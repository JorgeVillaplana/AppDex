"""
app.py
AppDex Dashboard - Aplicación Flask principal
"""

import json
import sqlite3
import configparser
from pathlib import Path
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__, static_folder='static', static_url_path='/static')


def _leer_config() -> Path:
    """Busca config.ini subiendo desde la ubicacion de app.py."""
    directorio = Path(__file__).resolve().parent
    for carpeta in [directorio, *directorio.parents]:
        candidato = carpeta / "config.ini"
        if candidato.exists():
            return candidato
    raise FileNotFoundError("No se encontro config.ini en ningun directorio padre.")


_config = configparser.ConfigParser()
_config.read(_leer_config(), encoding="utf-8")
DB_PATH = Path(_config.get("rutas", "base_de_datos"))


def get_db():
    con = sqlite3.connect(DB_PATH)
    con.row_factory = sqlite3.Row
    con.execute("PRAGMA foreign_keys = ON")
    return con


def get_catalogo(dominio, tabla_dominio):
    """Devuelve los valores de catálogo para un dominio y tabla dados."""
    con = get_db()
    cur = con.execute(
        "SELECT valor, descripcion FROM catalogos WHERE dominio = ? AND tabla_dominio = ? ORDER BY orden",
        (dominio, tabla_dominio)
    )
    valores = [dict(r) for r in cur.fetchall()]
    con.close()
    return valores


def get_catalogos_completos():
    """Devuelve todos los catálogos necesarios para el formulario."""
    return {
        "tipo":          get_catalogo("tipo", "herramientas"),
        "categoria":     get_catalogo("categoria", "herramientas"),
        "plataforma":    get_catalogo("plataforma", "herramientas"),
        "modelo_negocio":get_catalogo("modelo_negocio", "herramientas"),
        "opensource":    get_catalogo("opensource", "herramientas"),
        "vigencia":      get_catalogo("vigencia", "herramientas"),
    }


def get_lista(estado):
    """Devuelve la lista de herramientas en staging con el estado dado."""
    con = get_db()
    cur = con.execute(
        "SELECT id, nombre, url FROM herramientas_staging WHERE procesado = ? ORDER BY id",
        (estado,)
    )
    lista = [dict(r) for r in cur.fetchall()]
    con.close()
    return lista


def get_herramienta(herramienta_id):
    """Devuelve una herramienta de staging por su id."""
    con = get_db()
    cur = con.execute(
        "SELECT * FROM herramientas_staging WHERE id = ?",
        (herramienta_id,)
    )
    row = cur.fetchone()
    con.close()
    if not row:
        return None
    h = dict(row)
    # Deserializar JSON arrays
    for campo in ("categoria", "plataforma", "modelo_negocio"):
        try:
            h[campo] = json.loads(h[campo]) if h[campo] else []
        except (json.JSONDecodeError, TypeError):
            h[campo] = []
    return h


def get_siguiente_id(estado, id_actual):
    """Devuelve el id de la siguiente herramienta pendiente tras la actual."""
    con = get_db()
    cur = con.execute(
        "SELECT id FROM herramientas_staging WHERE procesado = ? AND id > ? ORDER BY id LIMIT 1",
        (estado, id_actual)
    )
    row = cur.fetchone()
    con.close()
    return row["id"] if row else None


@app.route("/")
def index():
    estado = request.args.get("estado", "Pendiente")
    herramienta_id = request.args.get("id", None)

    lista = get_lista(estado)

    # Si no se especifica id, cargamos la primera de la lista
    if not herramienta_id and lista:
        herramienta_id = lista[0]["id"]

    herramienta = get_herramienta(int(herramienta_id)) if herramienta_id else None
    catalogos = get_catalogos_completos()

    return render_template(
        "index.html",
        herramienta=herramienta,
        lista=lista,
        estado=estado,
        catalogos=catalogos,
    )


@app.route("/aprobar/<int:herramienta_id>", methods=["POST"])
def aprobar(herramienta_id):
    estado = request.form.get("estado", "Pendiente")
    con = get_db()
    try:
        # Serializar JSON arrays
        categoria      = json.dumps(request.form.getlist("categoria"), ensure_ascii=False)
        plataforma     = json.dumps(request.form.getlist("plataforma"), ensure_ascii=False)
        modelo_negocio = json.dumps(request.form.getlist("modelo_negocio"), ensure_ascii=False)

        con.execute("BEGIN")
        con.execute("""
            INSERT INTO herramientas (
                nombre, tipo, url, categoria, plataforma, descripcion,
                modelo_negocio, opensource, requiere_registro, version_estable,
                fecha_version, vigencia, icono_local, probada, notas,
                fecha_revision, origen
            ) VALUES (
                :nombre, :tipo, :url, :categoria, :plataforma, :descripcion,
                :modelo_negocio, :opensource, :requiere_registro, :version_estable,
                :fecha_version, :vigencia, :icono_local, :probada, :notas,
                :fecha_revision, :origen
            )
        """, {
            "nombre":           request.form.get("nombre"),
            "tipo":             request.form.get("tipo"),
            "url":              request.form.get("url"),
            "categoria":        categoria,
            "plataforma":       plataforma,
            "descripcion":      request.form.get("descripcion"),
            "modelo_negocio":   modelo_negocio,
            "opensource":       request.form.get("opensource"),
            "requiere_registro":1 if request.form.get("requiere_registro") == "1" else 0,
            "version_estable":  request.form.get("version_estable"),
            "fecha_version":    request.form.get("fecha_version"),
            "vigencia":         request.form.get("vigencia"),
            "icono_local":      request.form.get("icono_local"),
            "probada":          1 if request.form.get("probada") == "1" else 0,
            "notas":            request.form.get("notas"),
            "fecha_revision":   request.form.get("fecha_revision"),
            "origen":           "Dashboard",
        })
        con.execute(
            "UPDATE herramientas_staging SET procesado = 'Procesada' WHERE id = ?",
            (herramienta_id,)
        )
        con.commit()
    except Exception as e:
        con.rollback()
        raise e
    finally:
        con.close()

    siguiente = get_siguiente_id(estado, herramienta_id)
    if siguiente:
        return redirect(url_for("index", estado=estado, id=siguiente))
    return redirect(url_for("index", estado=estado))


@app.route("/omitir/<int:herramienta_id>", methods=["POST"])
def omitir(herramienta_id):
    estado = request.form.get("estado", "Pendiente")
    con = get_db()
    con.execute(
        "UPDATE herramientas_staging SET procesado = 'Omitida' WHERE id = ?",
        (herramienta_id,)
    )
    con.commit()
    con.close()

    siguiente = get_siguiente_id(estado, herramienta_id)
    if siguiente:
        return redirect(url_for("index", estado=estado, id=siguiente))
    return redirect(url_for("index", estado=estado))


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
