# 📋 Canonical Context

Resumen completo y ordenado de todo lo decidido hasta la fecha. Usar este documento para retomar el proyecto en cualquier sesión de trabajo o al iniciar una conversación con una IA.

Última actualización: 2026-04-29

---

## El proyecto

AppDex es un proyecto de creación de contenido multiplataforma. La idea central es presentar herramientas digitales como si fueran entradas de una Pokédex: un vídeo corto por herramienta, con tono narrativo inspirado en el doblaje español del anime de Pokémon.

Enfoque: eficiencia máxima con coste cero hasta rentabilidad. Objetivo: procesar una herramienta en menos de 60 segundos.

---

## La base de datos

Se eligió **SQLite** por ser local, gratuita, sin servidor y suficiente para el volumen del proyecto (500-600 herramientas).

### Arquitectura staging → producción

- **`herramientas_staging`**: datos sucios e incompletos. Las 585 herramientas actuales (580 + 5 que eran extras) están aquí pendientes de procesar.
- **`herramientas`**: datos limpios, completos y validados. Actualmente vacía.

### Decisiones de diseño relevantes

- `categoria`, `plataforma` y `modelo_negocio` son **JSON arrays** en SQLite. Esto permite múltiples valores sin tablas intermedias usando `json_each()`.
- La tabla `herramienta_extras` fue **eliminada**. Las herramientas subordinadas se insertan en `herramientas` y se relacionan con su padre mediante `Pertenece` en `herramienta_relaciones`.
- El campo `estado_contenido` fue **eliminado**. El control de contenido irá en tablas separadas (`contenido`, `contenido_youtube`...) en Fase 6.
- La tabla `catalogos` está **poblada** con todos los valores permitidos.
- `FOREIGN KEY` está activo. Activar explícitamente con `PRAGMA foreign_keys = ON` en cada conexión.

### Tablas principales

**`herramientas`**: Tabla de producción. Campos: id, nombre (UNIQUE), tipo, url (UNIQUE), categoria (JSON array), plataforma (JSON array), descripcion, modelo_negocio (JSON array), opensource, requiere_registro (0/1), version_estable, fecha_version, vigencia, icono_local, probada (0/1), notas, fecha_revision, fecha_alta, origen.

**`herramientas_staging`**: Bandeja de entrada. Todos los campos de `herramientas` más: procesado (`Pendiente`, `Omitida`, `Procesada`, `Migrada`), destino (`herramientas`), padre_nombre (para subordinadas).

**`herramienta_relaciones`**: Relaciones Pokémon. Campos: id, herramienta (FK), relacionada (FK), tipo (`Evolución`, `Simbiosis`, `Parentesco`, `Cohabitabilidad`, `Pertenece`), dirigida (0/1), notas.

**`catalogos`**: Valores permitidos. Campos: id, tabla_dominio, dominio, valor, descripcion, orden.

---

## Dashboard y Interfaz

- **Framework**: Flask (sin Docker por incompatibilidad SQLite + WSL2).
- **Arranque**: Doble clic en `run_dashboard.bat`.
- **Acceso local**: `http://localhost:5000`. Red local: `http://[IP-del-PC]:5000`.
- **Una sola pantalla** con todos los campos.
- **Panel lateral** con lista filtrable por `Pendiente` / `Omitida`.
- **Dos acciones**: Aprobar (→ `herramientas`) y Omitir (queda como `Omitida`).
- **Responsive**: Estructura preparada para móvil. Estilado pendiente para reducir tedio.

---

## Inteligencia Artificial Local (Ollama)

**Decisión estratégica**: Enfoque de **Entity Extraction (extracción de entidades)** no generación creativa. La IA extrae datos reales de las webs y los estructura en JSON.

### Configuración

- **Modelo**: Llama 3.1 8B (cuantización Q4_K_M).
- **Hardware**: GPU NVIDIA RTX 4060 (8GB VRAM). Cabe el modelo completo sin necesidad de CPU/RAM.
- **Contexto**: 4096 tokens (optimizado para VRAM).
- **Consumo eléctrico**: Insignificante (<1€/mes). Cada inferencia: 5-10 segundos.

### Riesgo identificado: alucinación por contexto ruidoso

Si se le manda HTML sucio a Ollama (con JS, CSS, menús, footers mezclados), puede sacar conclusiones erróneas. Por ejemplo, confundir el nombre de una distro Linux mencionada en un post del blog con el campo `version_estable`. **Solución**: limpiar el texto con Trafilatura antes de mandarlo, y diseñar el prompt con ejemplos explícitos de qué es y qué no es cada campo.

### Flujo de Integración (Fase 2b) — MVP

1. Usuario introduce URL de herramienta en Dashboard.
2. Script Python (scraper) hace GET a la landing con `requests` + User-Agent real.
3. `BeautifulSoup` extrae el HTML relevante.
4. `Trafilatura` limpia el texto descartando ruido (JS, CSS, nav, footer).
5. Texto limpio se envía a Ollama con prompt estructurado.
6. Ollama devuelve JSON con los campos que puede deducir de la landing.
7. Dashboard recibe JSON y rellena campos automáticamente.
8. Usuario revisa, completa manualmente lo que falte y guarda.

**Nota MVP**: El scraper visita solo la landing. Campos que no se puedan extraer (versión exacta, fecha, plataformas secundarias) se rellenan manualmente. El crawling automático por subpáginas es una mejora futura aparcada conscientemente.

**Beneficios**: Privacidad 100% (nada sale del PC), sin coste de API, sin límites de mensajes, integración directa con Dashboard.

---

## Web Scraping

### Estado actual del aprendizaje (2026-04-29)

Jorge ha completado el aprendizaje de los dos primeros bloques del scraper:

**`requests`** — dominado:
- Peticiones GET con headers personalizados
- Lectura de status code y body (`r.status_code`, `r.text`)
- User-Agent real extraído del propio navegador (Opera GX)
- Comprensión del ciclo request-response y de la IP pública

**`BeautifulSoup`** — dominado:
- Parseo de HTML con `html.parser`
- `find()` y `find_all()` por etiqueta y por clase (`class_`)
- `get_text(strip=True, separator=' ')` y limpieza de `\xa0`
- Comprensión de por qué buscar por etiqueta sola es frágil

**Pendiente**: Trafilatura (siguiente lección al volver del viaje).

### Decisiones de diseño del scraper

- **Librería HTTP**: `requests`
- **Parseo**: `BeautifulSoup`
- **Limpieza para IA**: `Trafilatura`
- **Ubicación durante desarrollo**: carpeta temporal en escritorio. Cuando esté maduro, se mueve a `Scripts/Python/scraper.py`
- **User-Agent**: el del propio navegador Opera GX del desarrollador

### Ética y técnica

- Revisar `robots.txt` de cada sitio antes de scrapear.
- Usar User-Agent realista para no ser bloqueado.
- Una petición por herramienta (no saturar servidores).
- El scraper es una ayuda, no una obligación. Para herramientas sin web o discontinuadas: relleno manual directo en Dashboard.

---

## Configuración Central

Archivo `config.ini` en raíz (`C:\AppDex\config.ini`). Rutas compartidas entre Python (`config.py`), PowerShell (`GenerarEstructura.ps1`) y Batch.

---

## Backup Automático

Script `backup_appdex.py` ejecutado diariamente a 00:30 via tarea programada de Windows.

- **Destino 1**: `E:\Jorge\AppDex_Backups\AppDex_YYYY-MM-DD_HH-MM-SS.db` (disco externo).
- **Destino 2**: `onedrive:AppDex\AppDex_YYYY-MM-DD_HH-MM-SS.db` (OneDrive vía rclone).

---

## Contenido y Producción

### Formato Pokédex

- **Presentación**: "AppDex número [N]. [Nombre]. Tipo [Categoría]."
- **Despedida (vídeos largos)**: "Y recordad, suscribíos para ser supereficaces, dadme un like crítico, comentad cual queréis que sea mi próximo movimiento y compartid con vuestra liga para llegar a ser unos maestros."
- **Duración guiones**: <120 palabras (aprox. 60 segundos con narrativa visual).

### Estrategia de Publicación

**Híbrida**: Contenido variado para testear qué categorías atraen más tráfico + Semanas Temáticas mensuales (ej. Ciberseguridad) para SEO del blog.

**Primera herramienta**: VirusTotal (decisión técnica y de nicho).

### Redes Sociales (2026)

| Plataforma | Formato | Rol |
|---|---|---|
| TikTok | Vídeo vertical 15-60s | Descubrimiento y viralidad |
| Instagram | Reels + Carruseles | Comunidad y guardado de fichas |
| X / Threads | Hilos de texto | Networking con programadores |
| BlueSky | Skeets | Nicho tech emergente |
| Pinterest | Pins / Infografías | Tráfico SEO al blog |
| YouTube | Shorts + Tutoriales | Monetización a largo plazo |

### Repurposing

"Crear una vez, publicar cinco": Un guion genera vídeo vertical (base), carruseles, infografías, hilos de texto para múltiples plataformas.

---

## Monetización

- **Afiliados**: URLs en tabla `contenido` (no en `herramientas`). Investigar programas de herramientas con comisión.
- **Blog SEO**: Catálogo completo + herramientas discontinuadas como curiosidades históricas (enlace a AlternativeTo genera tráfico cruzado).
- **Sponsors**: Contactar cuando llegue a 1.000-5.000 seguidores.
- **YouTube**: Requiere 1.000 suscriptores + 4.000 horas watch time.
- **Disclaimer de afiliados**: Obligatorio en todas las descripciones y blog (Ley de Publicidad).

---

## Aspectos Legales

- **Copyright Pokémon**: Inspiración + tono similar = Fair Use (parodia/transformación). Evitar logo oficial, música registrada o clips del anime.
- **Datos de hechos**: No tienen copyright. Versiones, precios, fechas son legales de extraer.
- **Obra derivada**: El formato Pokédex + redacción por IA propia = transformación, no plagio.
- **IA Transparency**: Considerar añadir "Guion asistido por IA" para transparencia legal.
- **Música**: Usar solo bibliotecas comerciales autorizadas para evitar desmonetización.
- **Scraping y TOS**: `robots.txt` es un convenio ético, no una ley. Lo que tiene fuerza legal son los Términos de Servicio de cada web. El scraping manual (una URL a la vez, iniciado por el usuario) es de bajo riesgo legal. El scraping masivo automatizado es donde surgen los problemas.
- **IP pública**: Queda registrada en los logs del servidor. Las peticiones del scraper no son anónimas.

---

## Tecnología Stack Actual

| Componente | Tecnología | Notas |
|---|---|---|
| Base de datos | SQLite | Local, sin servidor |
| Backend | Python 3.x | Scripts de automatización |
| Web framework | Flask | Dashboard local |
| Frontend | HTML5 / CSS3 | Responsive, sin JavaScript framework |
| IA Local | Ollama + Llama 3.1 8B | Entity extraction, no generación creativa |
| Scraping HTTP | requests | Peticiones GET con User-Agent real |
| Scraping parseo | BeautifulSoup | Extracción de elementos HTML |
| Scraping limpieza | Trafilatura | Texto limpio para Ollama (pendiente de aprender) |
| Versionado | Git + GitHub | Cuando haya 4-5 scripts Python |
| Contenido | ElevenLabs | Voz IA (Fase 4) |
| Blog | Astro | Framework estático (Fase 5) |

---

## Pendiente Inmediato

- **Trafilatura**: Siguiente lección del dojo de scraping al volver del viaje (2026-04-29+4 días).
- **Estilado del Dashboard**: Hacerlo visualmente agradable para reducir tedio del procesado.
- **Botones de IA en Dashboard**: Añadir "Sugerir con Ollama" al lado de campos.
- **Gestión de JSON arrays en formulario**: Asegurar que selectores múltiples funcionan correctamente.

## Pendiente Aparcado Conscientemente

- **Crawling automático**: Scraper que navega solo por subpáginas. Complejidad alta, no necesario para MVP.
- **Script de migración**: Hasta que no haya ~100 herramientas procesadas no se toca.
- **Notion API sync**: Cuando el flujo manual esté estable.
- **Docker**: Retomado cuando haya homelab Linux.
- **Blog**: Fase 5, después de producir contenido piloto.
