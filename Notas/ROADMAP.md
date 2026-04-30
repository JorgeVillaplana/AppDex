# 🗺️ Hoja de ruta

Estado y orden de las tareas del proyecto AppDex.

---

## ✅ Completado

- [x] Diseño del esquema de base de datos (v2 final)
- [x] Migración de 585 herramientas a `herramientas_staging`
- [x] Tabla `catalogos` poblada
- [x] Configuración central `config.ini`
- [x] Dashboard funcional (Flask)
- [x] Estructura HTML responsive
- [x] CSS base sin estilar
- [x] Aprendizaje de `requests`: peticiones HTTP, status codes, headers, User-Agent
- [x] Aprendizaje de `BeautifulSoup`: parseo HTML, find(), find_all(), get_text(), selección por clase

---

## 🔜 Próximos pasos (en orden)

### Fase 2 — Dashboard (mejoras inmediatas)
- [ ] **Estilado visual**: Que sea agradable para reducir tedio
- [ ] **Altura viewport fija**: Que ocupe exactamente la pantalla
- [ ] **Scrolls independientes**: Lista y formulario cada uno con su scroll

### Fase 2b — Web Scraping + IA Local
- [ ] **Trafilatura**: Aprender a limpiar HTML crudo antes de mandarlo a Ollama ← SIGUIENTE
- [ ] Instalar y configurar Ollama (Llama 3.1 8B Q4_K_M)
- [ ] Diseñar prompt preciso para evitar alucinaciones (especialmente en campos como `version_estable`)
- [ ] Implementar script de scraping completo (requests + BeautifulSoup + Trafilatura)
- [ ] Integrar Ollama en Dashboard vía API local
- [ ] Añadir botones "Sugerir con IA" en formulario
- [ ] Validar flujo: URL → Scrape → Trafilatura → Ollama → JSON → Campos rellenos

### Fase 3 — Procesado del catálogo
- [ ] Procesar ~100 herramientas de staging a través del Dashboard mejorado
- [ ] Validar que el flujo no tiene fatiga ni errores

### Fase 3b — Script de Migración
- [ ] Una vez probado el flujo manual con 100 herramientas, desarrollar script de migración
- [ ] Procesa herramientas con `procesado = 'Procesada'`
- [ ] Inserta en `herramientas`
- [ ] Si tiene `padre_nombre`, crea relación `Pertenece` en `herramienta_relaciones`
- [ ] Marca como `Migrada` en staging

### Fase 4 — Producción de Contenido
- [ ] Definir estructura exacta del guion (formato Pokédex)
- [ ] Crear plantilla rígida de guion (Intro, Lore, Stats, Captura)
- [ ] Grabar vídeo piloto con herramienta elegida (VirusTotal)
- [ ] Configurar ElevenLabs (voz IA)
- [ ] Validar duración y formato

### Fase 5 — Blog
- [ ] Decidir stack final (candidato: Astro)
- [ ] Diseñar estructura del blog
- [ ] Conectar blog con SQLite para generación automática

### Fase 6 — Monetización
- [ ] Diseñar tablas de contenido (`contenido`, `contenido_youtube`...)
- [ ] Investigar programas de afiliados de herramientas prioritarias
- [ ] Configurar AdSense en blog

### Fase 7 — Automatización Futura
- [ ] Crawling automático: scraper que navega solo por subpáginas relevantes (/download, /pricing) siguiendo enlaces internos
- [ ] Script de sync Notion → `herramientas_staging`
- [ ] Script de limpieza de Notion (borra lo procesado)
- [ ] GitHub con 4-5 scripts Python (no subir AppDex.db ni Obsidian)

---

## 📌 Notas de Prioridad

- El Dashboard es el cuello de botella. Si no es cómodo, el proyecto fracasa por tedio.
- La integración de scraping + Ollama es crítica para que procesar una herramienta lleve <60 segundos.
- El scraper del MVP visita solo la landing. Campos que no se puedan extraer se rellenan manualmente. El crawling automático es una mejora futura, no un requisito.
- No comenzar migración masiva hasta tener 100 herramientas validadas.
- Las semanas temáticas son para SEO del blog, no imprescindibles al lanzar.
- Los tutoriales largos son expansión futura, no requisito inicial.
