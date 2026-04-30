# 📄 Archivos importantes

Listado de archivos clave del proyecto y el motivo de su relevancia.

---

| Archivo                         | Ruta                    | Relevancia                                                                                                               |
| ------------------------------- | ----------------------- | ------------------------------------------------------------------------------------------------------------------------ |
| `AppDex.db`                     | `Database/`             | ⭐ La base de datos principal. Es la fuente de verdad de todo el proyecto. Hacer copias de seguridad regularmente.        |
| `AppDex.sqbpro`                 | `Database/`             | Archivo de proyecto de DB Browser for SQLite. Guarda la configuración de la interfaz visual.                             |
| `CREATE_TABLES_26-04-26.txt`    | `Database/Scripts/DDL/` | DDL original v1. Referencia histórica.                                                                                   |
| `CREATE_TABLES_26-04-26_v2.txt` | `Database/Scripts/DDL/` | ⭐ DDL actualizado v2. Esquema actual de la base de datos. Imprescindible si hay que recrear la base de datos desde cero. |
| `INSERT_CATALOGOS_26-04-26.txt` | `Database/Scripts/DML/` | ⭐ Script SQL para poblar la tabla `catalogos` con todos los valores permitidos.                                          |
| `megaexport.csv`                | `Database/CSVs/`        | Exportación original en bruto de Notion, Raindrop y Opera GX. Guardar como referencia histórica, no modificar.           |
| `appdex_limpio.csv`             | `Database/CSVs/`        | CSV limpio y revisado manualmente. Fuente de la importación inicial. Guardar como referencia histórica.                  |
| `config.ini`                    | Raíz del proyecto       | ⭐ Archivo de configuración central. Contiene todas las rutas del proyecto. Leído por Python y PowerShell.                |
| `config.py`                     | `Scripts/Python/`       | ⭐ Módulo Python reutilizable para leer `config.ini`. Importar con `from config import cfg` en cualquier script.          |
| `importar_csv.py`               | `Scripts/Python/`       | Script Python de importación inicial del CSV a SQLite. Útil si hay que repetir la importación desde cero.                |
| `migrar_schema_v2.py`           | `Scripts/Python/`       | Script Python de migración del esquema v1 → v2. Ya ejecutado. Guardar como referencia histórica.                         |
| `backup_appdex.py`              | `Scripts/Python/`       | ⭐ Script de backup automático. Se ejecuta diariamente a las 00:30 via tarea programada de Windows.                       |
| `GenerarEstructura.ps1`         | `Scripts/Otros/`        | Script PowerShell que genera el árbol de `ESTRUCTURA.md`. Lee rutas desde `config.ini`.                                  |
| `run_generarEstructura.bat`     | `Scripts/Otros/`        | Lanza `GenerarEstructura.ps1` con doble clic.                                                                            |
| `app.py`                        | `Dashboard/`            | ⭐ Aplicación Flask principal del Dashboard.                                                                              |
| `index.html`                    | `Dashboard/templates/`  | ⭐ Template HTML del Dashboard. Vista única con todos los campos de enriquecimiento.                                      |
| `requirements.txt`              | `Dashboard/`            | Dependencias Python del Dashboard.                                                                                       |
| `run_dashboard.bat`             | `Dashboard/`            | ⭐ Arranca el Dashboard con doble clic.                                                                                   |

---

## Archivos pendientes de crear

| Archivo | Ruta prevista | Descripción |
|---|---|---|
| `sync_notion.py` | `Scripts/Python/` | Script de sincronización Notion → `herramientas_staging` |
| `migrar_staging.py` | `Scripts/Python/` | Script de migración staging → producción (`procesado = 'Procesada'` → `herramientas`) |
| `limpiar_notion.py` | `Scripts/Python/` | Script que borra de Notion las entradas ya procesadas |

---

## Copias de seguridad

`AppDex.db` es el archivo más crítico del proyecto. El backup automático está configurado y funcionando:

- **Destino 1**: `E:\Jorge\AppDex_Backups\AppDex_YYYY-MM-DD_HH-MM-SS.db` (disco duro externo)
- **Destino 2**: `onedrive:AppDex\AppDex_YYYY-MM-DD_HH-MM-SS.db` (OneDrive vía rclone)
- Guarda versiones con fecha, nunca sobreescribe.

Además, antes de cualquier operación masiva sobre la base de datos, hacer siempre una copia manual previa.
