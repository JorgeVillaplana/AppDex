"""
config.py
AppDex - Módulo de configuración central

Uso en cualquier script Python del proyecto:

    from config import cfg

    db_path   = cfg.base_de_datos
    notas     = cfg.notas
    proyecto  = cfg.proyecto

El módulo busca config.ini subiendo desde su propia ubicación
hasta encontrarlo, por lo que funciona independientemente de
desde dónde se ejecute el script.
"""

import configparser
import sys
from pathlib import Path


def _encontrar_config() -> Path:
    """
    Busca config.ini subiendo por el árbol de directorios
    desde la ubicación de este archivo.
    """
    directorio = Path(__file__).resolve().parent
    for carpeta in [directorio, *directorio.parents]:
        candidato = carpeta / "config.ini"
        if candidato.exists():
            return candidato
    raise FileNotFoundError(
        "No se encontró config.ini en ningún directorio padre. "
        "Asegúrate de que config.ini está en la raíz del proyecto (C:\\AppDex)."
    )


class _Config:
    """
    Clase que expone los valores de config.ini como atributos.
    Se instancia una sola vez al importar el módulo.
    """

    def __init__(self):
        ruta_ini = _encontrar_config()
        parser = configparser.ConfigParser()
        parser.read(ruta_ini, encoding="utf-8")

        # [rutas]
        self.proyecto       = Path(parser.get("rutas", "proyecto"))
        self.base_de_datos  = Path(parser.get("rutas", "base_de_datos"))
        self.notas          = Path(parser.get("rutas", "notas"))
        self.scripts_python = Path(parser.get("rutas", "scripts_python"))
        self.scripts_otros  = Path(parser.get("rutas", "scripts_otros"))
        self.media          = Path(parser.get("rutas", "media"))
        self.iconos         = Path(parser.get("rutas", "iconos"))
        self.estructura_md  = Path(parser.get("rutas", "estructura_md"))
        self.backup_local   = Path(parser.get("rutas", "backup_local"))
        self.backup_remoto  = parser.get("rutas", "backup_remoto")  # string, no Path

        # [configuracion]
        ignorar_raw = parser.get("configuracion", "ignorar_estructura")
        self.ignorar_estructura = [x.strip() for x in ignorar_raw.split(",")]

    def __repr__(self):
        return f"<Config proyecto={self.proyecto}>"


# Instancia única compartida por todos los scripts que importen este módulo
cfg = _Config()


if __name__ == "__main__":
    # Ejecuta este archivo directamente para verificar que todo se lee bien:
    # python config.py
    if sys.stdout.encoding and sys.stdout.encoding.lower() != "utf-8":
        sys.stdout.reconfigure(encoding="utf-8")

    print("=== Verificacion de config.ini ===\n")
    print(f"  proyecto        : {cfg.proyecto}")
    print(f"  base_de_datos   : {cfg.base_de_datos}")
    print(f"  notas           : {cfg.notas}")
    print(f"  scripts_python  : {cfg.scripts_python}")
    print(f"  scripts_otros   : {cfg.scripts_otros}")
    print(f"  media           : {cfg.media}")
    print(f"  iconos          : {cfg.iconos}")
    print(f"  estructura_md   : {cfg.estructura_md}")
    print(f"  backup_local    : {cfg.backup_local}")
    print(f"  backup_remoto   : {cfg.backup_remoto}")
    print(f"  ignorar         : {cfg.ignorar_estructura}")
    print("\n=== OK ===")
