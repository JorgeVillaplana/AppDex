# 🛠️ Tecnologías

Listado de tecnologías utilizadas, en uso o previstas para el proyecto AppDex.

---

## ✅ En uso actualmente

| Tecnología | Rol | Notas |
|---|---|---|
| **SQLite** | Base de datos local principal | Sin servidor, archivo único, portable |
| **DB Browser for SQLite** | Interfaz visual para SQLite | Gratuito, open source |
| **Python** | Scripting y automatización | Versión 3.x |
| **Flask** | Framework web para el Dashboard local | Más sencillo que FastAPI, suficiente para un dashboard de un solo usuario |
| **LibreOffice Calc** | Revisión y edición de CSVs | Alternativa gratuita a Excel |
| **Obsidian** | Gestión del vault / documentación | La carpeta AppDex es el vault |
| **Notion** | Bandeja de entrada de nuevas herramientas | Solo para ingesta futura, no como BD principal |
| **Opera GX** | Navegador con marcadores exportados | Fuente original de parte del catálogo |
| **Raindrop.io** | Gestor de marcadores | Fuente original de parte del catálogo |
| **rclone** | Sincronización de backups con OneDrive | Ejecutado desde Python vía subprocess |
| **Docker Desktop** | Contenedores | Instalado con WSL2. Aparcado para el Dashboard hasta disponer de homelab Linux |

---

## 🔜 Previstas a corto plazo

| Tecnología | Rol | Notas |
|---|---|---|
| **Ollama** | IA local para sugerencias en el Dashboard | Modelos candidatos: Llama 3.1 8B o Mistral 7B. Sin coste ni límites |
| **Notion API** | Sincronización automática desde Notion a SQLite | Plan gratuito, suficiente para el volumen previsto |

---

## 🗺️ Previstas a medio-largo plazo

| Tecnología | Rol | Notas |
|---|---|---|
| **TikTok / YouTube Shorts / Instagram Reels** | Publicación de vídeos cortos | Multiplataforma, automatizar publicación |
| **Make (ex-Integromat)** o **Buffer** | Automatización de publicación en RRSS | Ambos tienen tier gratuito |
| **ElevenLabs** | Narración de vídeos con voz IA | Plan gratuito para empezar |
| **PowerDirector** | Edición de vídeos | Gratuito, candidato principal |
| **Blog** | Referencia escrita de todas las herramientas presentadas | También como portfolio y activo SEO |
| **Astro** | Framework para el blog estático | Rápido, gratuito, compatible con SQLite |
| **Windows Sandbox** | Entorno seguro para probar herramientas | Para tutoriales largos a futuro |

---

## 📝 Notas importantes

- Se prioriza **software gratuito** en todas las fases del proyecto.
- La base de datos es **local** por decisión consciente: sin dependencia de internet, sin coste de servidor, sin riesgo de pérdida de acceso.
- La integración con Notion es **unidireccional**: Notion → SQLite. La fuente de verdad siempre es SQLite.
- El Dashboard corre directamente en Windows con Flask (sin Docker) debido a incompatibilidades de SQLite con Docker + WSL2 sobre sistemas de archivos de Windows. Docker se retoma cuando haya un homelab Linux.
- El blog podría migrar a PostgreSQL en el futuro si necesita acceso concurrente, pero SQLite es suficiente para la fase inicial.
