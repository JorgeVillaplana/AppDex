# 💡 Sugerencias de mejora

Ideas identificadas durante el desarrollo del proyecto.

---

## Dashboard

- **Estilado visual**: Hacerlo agradable reduce el tedio del procesado masivo
- **Ocupar viewport completo**: Altura 100vh sin scrolls globales
- **Scrolls independientes**: Lista lateral y formulario cada uno con su propio scroll
- **Botones de IA**: "Sugerir con Ollama" al lado de campos vaciados
- **Validación en tiempo real**: Alertar si campos obligatorios están vacíos antes de guardar

---

## Web Scraping + IA Local

- **Script de scraper**: Integrar requests + BeautifulSoup en Dashboard
- **Flujo de inferencia**: URL → Scrape → Ollama → JSON → Campos → Usuario valida
- **Caché de scrapes**: Guardar texto extraído para reutilizar sin re-scrapear
- **Manejo de errores**: Si scraper falla, permitir input manual de texto
- **Prompt refinado**: Perfeccionar instrucciones a Ollama para que las sugerencias sean cada vez mejores

---

## Procesado de Herramientas

- **Sprints cortos**: 20-30 minutos de procesado, no sesiones maratónicas
- **Nota de sesión**: Al terminar cada sesión, apuntar qué se hizo en Obsidian
- **Notificaciones visuales**: Indicador de progreso (ej. "42/100 herramientas procesadas")

---

## Contenido y Producción

- **Plantilla rígida de guion**: Estructura fija (Intro, Lore, Stats, Captura) para consistencia
- **Validación de duración**: Sistema que alerte si el guion excede 120 palabras (~60 segundos)
- **Primeras 10 herramientas**: Priorizar las que tengan programas de afiliados jugosos
- **VirusTotal como piloto**: Primera herramienta para validar flujo completo (grabación, edición, publicación)
- **Vídeo piloto con ElevenLabs**: Grabar piloto antes de procesar 585, para validar formato

---

## Monetización y Estrategia

- **Investigación de afiliados**: Mapear herramientas con comisión antes de grabar
- **Semanas temáticas mensuales**: Agrupar contenido por categoría una vez al mes
- **Blog SEO**: Herramientas discontinuadas como "curiosidades históricas" con enlace a AlternativeTo
- **Disclaimer de afiliados**: Obligatorio en descripción de vídeo y blog
- **Repurposing**: Un guion → Vídeo Vertical + Carruseles + Infografías + Threads + Skeets

---

## Técnico

- **Control de versiones del esquema**: Mantener la convención de scripts con fecha en `Database/Scripts/DDL/`
- **GitHub cuando sea momento**: Crear repositorio cuando haya 4-5 scripts Python (nunca subir AppDex.db)
- **Migración a PostgreSQL**: Solo si el blog escala y necesita acceso concurrente (no necesario ahora)
- **Chequeo periódico automático**: Script que revise `fecha_revision` y actualice `vigencia` consultando GitHub API o scraping ligero
- **Descarga masiva de iconos**: Script que descargue favicons faltantes automáticamente

---

## Legal

- **Ética de scraping**: Respetar robots.txt, usar User-Agent realista, no saturar servidores
- **Disclaimer Pokémon**: "Inspiración en la Pokédex. No afiliado a The Pokémon Company"
- **Música comercial**: Usar solo bibliotecas autorizadas (Epidemic Sound, Artlist, etc.)
- **IA Transparency**: Considerar añadir "Guion asistido por IA local" para transparencia
- **Datos de hechos**: Versiones, precios, fechas no tienen copyright y se pueden extraer libremente
