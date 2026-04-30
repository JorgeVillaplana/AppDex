# 🗂️ AppDex

> *"Gotta catalog 'em all"*

AppDex es un proyecto personal de creación de contenido cuyo objetivo es catalogar, clasificar y presentar herramientas digitales de forma entretenida, inspirándose en el formato de la Pokédex tal y como aparece en el anime de Pokémon en España.

---

## 📌 Índice

- [Objetivo](#objetivo)
- [Concepto creativo](#concepto-creativo)
- [Estado actual](#estado-actual)
- [Estructura del proyecto](./ESTRUCTURA.md)
- [Tecnologías](./TECNOLOGIAS.md)
- [Base de datos](./DATABASE.md)
- [Canonical context](./CANONICAL_CONTEXT.md)
- [Hoja de ruta](./ROADMAP.md)
- [Sugerencias de mejora](./MEJORAS.md)

---

## Objetivo

Crear un canal de contenido multiplataforma centrado en la presentación de herramientas digitales (aplicaciones, servicios web, utilidades, recursos) mediante vídeos cortos con formato y tono inspirado en la Pokédex del anime de Pokémon.

A medio-largo plazo, el proyecto contempla:

- Vídeos cortos para redes sociales (TikTok, YouTube Shorts, Instagram Reels...)
- Blog de referencia con todas las herramientas presentadas
- Vídeos largos de tutoriales de instalación y uso
- Posible monetización vía afiliación, sponsors y AdSense

---

## Concepto creativo

Cada herramienta es tratada como si fuera un Pokémon. La presentación sigue el estilo de la Pokédex española: tono narrativo, datos concretos, y una entrada por herramienta.

Las relaciones entre herramientas se modelan con terminología Pokémon:

| Tipo de relación | Significado | Dirigida |
|---|---|---|
| Evolución | A da lugar a B, no al revés | Sí |
| Simbiosis | Se necesitan mutuamente | No |
| Parentesco | Mismo origen o familia | No |
| Cohabitabilidad | Funcionan bien juntas | No |
| Pertenece | A forma parte de B (jerarquía) | Sí |

---

## Estado actual

- [x] Diseño del esquema de base de datos
- [x] Creación de tablas en SQLite
- [x] Exportación y limpieza del catálogo inicial (~580 herramientas)
- [x] Importación a la base de datos
- [ ] Clasificación y catalogación de herramientas (categoría, tipo, vigencia...)
- [ ] Integración con Notion para ingesta futura de herramientas
- [ ] Producción de contenido
- [ ] Blog
