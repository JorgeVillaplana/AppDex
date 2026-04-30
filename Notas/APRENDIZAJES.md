# 🧠 Aprendizajes y Stack de capacidades

Documento de seguimiento del aprendizaje de Jorge a lo largo del proyecto AppDex.

---

## ✅ Stack tecnológico dominado

- **Python** (nivel intermedio): scripting, automatización, manejo de ficheros
- **SQL** (nivel intermedio): diseño relacional, transacciones, JSON nativo en SQLite
- **Web**: HTML5, CSS3 (nivel básico-intermedio)
- **Git y GitHub**: control de versiones
- **Windows 11 + PowerShell + Batch**: administración del sistema
- **SQLite**: diseño de esquemas, tipos de datos, PRAGMA, transacciones

---

## 📚 Aprendido durante AppDex

### Bases de datos

| Concepto | Estado |
|---|---|
| JSON arrays en SQLite | Aprendido ✅ |
| Transacciones (BEGIN/COMMIT/ROLLBACK) | Aprendido ✅ |
| Tablas internas (sqlite_stat1, sqlite_sequence) | Aprendido ✅ |
| FOREIGN KEY e integridad referencial | Aprendido ✅ |
| Arquitectura staging → producción | Aprendido ✅ |
| Grafos dirigidos y relaciones complejas | Aprendido ✅ |

### Web y Frontend

| Concepto | Estado |
|---|---|
| Flask (rutas, templates Jinja2, formularios POST) | Aprendido ✅ |
| HTML responsivo + CSS variables | Aprendido ✅ |
| Grid layout y flexbox | Aprendido ✅ |
| Manejo de formularios con multiselect | Aprendido ✅ |

### Configuración e Infraestructura

| Concepto | Estado |
|---|---|
| Archivos `config.ini` compartidos | Aprendido ✅ |
| `configparser` Python | Aprendido ✅ |
| Lectura de config en PowerShell | Aprendido ✅ |
| Codificación UTF-8 en consola Windows | Aprendido ✅ |
| Backup automático con versionado | Aprendido ✅ |
| Tarea programada de Windows | Aprendido ✅ |

### IA Local

| Concepto | Descripción | Estado |
|---|---|---|
| **Entity Extraction** | Uso de IA para identificar y categorizar datos específicos en texto desordenado | Aprendido ✅ |
| **Grounding (Anclaje)** | Alimentar a la IA con datos reales externos para evitar alucinaciones | Aprendido ✅ |
| **Tokens y Context Window** | Unidad mínima de procesamiento y limitación de "memoria de trabajo" de la IA | Aprendido ✅ |
| **Cuantización de modelos** | Compresión (ej. 16 bits → 4 bits) para que quepan en hardware doméstico | Aprendido ✅ |
| **Alucinación por contexto ruidoso** | Si se le manda texto sucio a Ollama, puede sacar conclusiones erróneas (ej. confundir "Fedora" con una versión de software). Solución: limpiar bien antes de mandar | Aprendido ✅ |
| **Inferencia local con Ollama** | Ejecución de modelos LLM sin coste de API | Por aprender 🔜 |

### Web Scraping

| Concepto | Descripción | Estado |
|---|---|---|
| **HTTP request-response cycle** | Modelo cliente-servidor: el cliente manda GET, el servidor responde con HTML + status code + headers. Base de todo el scraping | Aprendido ✅ |
| **Status codes HTTP** | 200 OK, 403 Prohibido, 404 No existe, 429 Demasiadas peticiones, 503 Caído. El scraper debe reaccionar a cada uno | Aprendido ✅ |
| **Headers y User-Agent** | Metadatos que viajan con la petición. El User-Agent identifica al cliente. Sin configurar, Python se identifica como bot y puede ser bloqueado | Aprendido ✅ |
| **IP pública y bloqueo por IP** | El servidor ve tu IP pública, no tu dispositivo. Peticiones masivas desde la misma IP pueden resultar en bloqueo (429/403) | Aprendido ✅ |
| **robots.txt** | Estructura: bloques `User-agent` + directivas `Allow`/`Disallow`. Solo aplica a bots, nunca a navegadores. `Allow: /` es el más permisivo. `Disallow: /` bloquea todo | Aprendido ✅ |
| **SPA vs web estática** | Las SPAs renderizan contenido con JavaScript en el cliente. `requests` solo descarga el HTML inicial, que en una SPA puede estar vacío. Para webs estáticas, `requests` es suficiente | Aprendido ✅ |
| **requests** | Librería Python para peticiones HTTP. `requests.get(url, headers=headers)`. Respuesta: `.status_code`, `.text` | Aprendido ✅ |
| **BeautifulSoup** | Parseo y extracción de datos del HTML. `find()` devuelve el primer elemento, `find_all()` devuelve lista. Buscar por etiqueta + clase con `class_` | Aprendido ✅ |
| **get_text() y limpieza** | `.get_text(strip=True)` elimina espacios y saltos. `.get_text(separator=' ')` evita concatenación sin espacios. `.replace('\xa0', ' ')` limpia `&nbsp;` | Aprendido ✅ |
| **Entidades HTML** | Caracteres especiales como `&nbsp;` (espacio), `&amp;` (`&`), `&lt;` (`<`). BeautifulSoup los convierte a Unicode al parsear | Aprendido ✅ |
| **Selección precisa por clase** | Buscar por etiqueta sola es frágil. Combinar etiqueta + clase semánticamente significativa da selectores más robustos (`soup.find("p", class_="text-muted")`) | Aprendido ✅ |
| **Límites del scraping** | Texto en imágenes, SVGs, SPAs, contenido tras login y canvas son difíciles o imposibles sin herramientas adicionales. La descripción de marketing casi siempre está en HTML plano por SEO | Aprendido ✅ |
| **Scraping multipágina** | La info relevante no siempre está en la landing. A veces hay que visitar 2-3 URLs del mismo dominio (landing + /download + /pricing) y combinar resultados | Aprendido ✅ |
| **Crawling automático** | Scraper que navega solo siguiendo enlaces internos. Complejidad considerable (bucles, profundidad, filtrado). Aparcado para fase futura | Por aprender 🔜 |
| **DOM (Document Object Model)** | Árbol de etiquetas HTML que compone una página web | Aprendido ✅ |
| **Trafilatura** | Librería para extracción de contenido limpio descartando JS, CSS, menús y footers. Paso intermedio entre BeautifulSoup y Ollama | Por aprender 🔜 |

---

## 🧩 Habilidades blandas observadas

### Puntos fuertes

- **Diseño defensivo**: Anticipa problemas y pregunta por casos edge
- **Pensamiento sistémico**: Ve implicaciones de cada decisión en el sistema global
- **Sentido crítico**: No acepta propuestas sin cuestionarlas
- **Pragmatismo**: Sabe cuándo parar y avanzar ("cada problema a su momento")
- **Gestión del alcance**: Identifica y aparca tareas prematuras
- **Documentación**: Valida la importancia y lo hace desde el principio
- **Visión de negocio**: Detecta oportunidades (herramientas discontinuadas en blog, SEO, monetización)
- **Análisis de producto**: Detecta problemas reales antes de que estén en producción (ej. alucinación por contexto ruidoso, herramientas sin web oficial)

### Áreas a trabajar

- **Tedio en procesado masivo**: Riesgo de abandono. Solución: Dashboard eficiente + Ollama
- **Markdown y Obsidian avanzado**: Conocimiento básico, profundizar después
- **Scope creep**: Tendencia a querer resolver problemas futuros antes de terminar el actual. Detectado y controlado conscientemente ✅

---

## 🗺️ Próximos aprendizajes previstos

1. **Trafilatura**: Extracción de texto limpio para alimentar a Ollama
2. **Ollama**: Instalación, configuración, API local, integración con Python
3. **Crawling básico**: Seguir enlaces internos de forma controlada (fase futura)
4. **Voz IA**: ElevenLabs
5. **Astro**: Framework de blog estático
6. **Automatización de RRSS**: Make o Buffer
7. **Estrategia de contenido**: AEO, repurposing, micro-copywriting

---

## 💡 Aprendizajes Especiales

**"Del usuario de IA al arquitecto de flujos de datos"**: Jorge ha pasado de pedir que la IA genere contenido a diseñar un sistema donde la IA extrae datos reales, estructurados, validados por humanos. Esto es un cambio fundamental de mentalidad — prioridad a utilidad y ahorro de tiempo sobre novedad tecnológica.

**"Haz que funcione primero, luego hazlo mejor"**: Regla de oro del desarrollo aplicada conscientemente. El crawling automático es una optimización futura, no un requisito del MVP. El scraper del MVP visita URLs conocidas, el usuario valida el resto manualmente.
