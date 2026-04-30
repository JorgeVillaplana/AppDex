# 🗄️ Base de datos

AppDex usa **SQLite** como base de datos local. El archivo principal es `Database/AppDex.db`.

---

## Tablas

### `herramientas`
Tabla principal de producción. Almacena herramientas, recursos, directorios y similares ya procesados y validados. **Actualmente vacía** — las herramientas se procesan desde `herramientas_staging` a través del Dashboard.

| Campo | Tipo | Descripción |
|---|---|---|
| `id` | INTEGER PK | Autoincremental, nunca se reutiliza |
| `nombre` | TEXT UNIQUE | Nombre de la herramienta |
| `tipo` | TEXT | Ver tabla `catalogos`. Valores: `Herramienta`, `Recurso`, `Directorio`, `Documentacion`, `Repositorio`, `Foro` |
| `url` | TEXT UNIQUE | URL principal |
| `categoria` | TEXT | JSON array. Ej: `["Diseño", "IA"]`. Ver tabla `catalogos` |
| `plataforma` | TEXT | JSON array. Ej: `["Windows", "Web"]`. Ver tabla `catalogos` |
| `descripcion` | TEXT | Descripción libre de la herramienta |
| `modelo_negocio` | TEXT | JSON array. Ej: `["Freemium", "Suscripción"]`. Ver tabla `catalogos` |
| `opensource` | TEXT | `Sí`, `No`, `Desconocido` |
| `requiere_registro` | INTEGER | 0 = No, 1 = Sí |
| `version_estable` | TEXT | Última versión estable conocida |
| `fecha_version` | TEXT | Fecha de la versión (YYYY-MM-DD) |
| `vigencia` | TEXT | `Activa`, `Sin mantenimiento`, `Desaconsejada`, `Discontinuada` |
| `icono_local` | TEXT | Ruta al icono descargado (relativa a `Media/icons/`) |
| `probada` | INTEGER | 0 = No probada, 1 = Probada personalmente |
| `notas` | TEXT | Notas libres |
| `fecha_revision` | TEXT | Fecha del último chequeo (YYYY-MM-DD) |
| `fecha_alta` | TEXT | Fecha de inserción, automática (YYYY-MM-DD) |
| `origen` | TEXT | `CSV`, `Notion`, `Manual`, `Dashboard` |

---

### `herramientas_staging`
Bandeja de entrada. Contiene las 585 herramientas pendientes de procesar (580 originales + 5 que eran extras). Las herramientas pasan por el Dashboard y se migran a `herramientas` una vez validadas.

Tiene los mismos campos que `herramientas` más los siguientes exclusivos de staging:

| Campo | Tipo | Descripción |
|---|---|---|
| `procesado` | TEXT | `Pendiente`, `Omitida`, `Procesada`, `Migrada` |
| `destino` | TEXT | `herramientas` (único valor actual) |
| `padre_nombre` | TEXT | Nombre del padre si es una herramienta subordinada. Se resuelve a un id durante la migración |

**Flujo de `procesado`:**
```
Pendiente → Omitida → Pendiente (se recupera)
Pendiente → Procesada (validada en Dashboard)
Procesada → Migrada (script de migración)
```

---

### `herramienta_relaciones`
Modela relaciones entre herramientas al estilo Pokédex. **Reemplaza a la antigua tabla `herramienta_extras`**, que fue eliminada. Las herramientas subordinadas ahora se insertan en `herramientas` y se relacionan con su padre mediante una relación de tipo `Pertenece`.

| Campo | Tipo | Descripción |
|---|---|---|
| `id` | INTEGER PK | Autoincremental |
| `herramienta` | INTEGER FK | Origen de la relación |
| `relacionada` | INTEGER FK | Destino de la relación |
| `tipo` | TEXT | Ver tipos de relación más abajo |
| `dirigida` | INTEGER | 0 = Bidireccional, 1 = Unidireccional |
| `notas` | TEXT | Notas libres |

**Tipos de relación:**

| Tipo | Dirigida | Descripción |
|---|---|---|
| `Evolución` | Sí | Una herramienta da lugar a otra; la original queda obsoleta o absorbida. Va de predecesora a sucesora |
| `Simbiosis` | No | Se necesitan mutuamente para funcionar o aportar su valor completo |
| `Parentesco` | No | Comparten origen, empresa, ecosistema o filosofía sin dependencia entre ellas |
| `Cohabitabilidad` | No | Funcionan bien juntas y se recomiendan en combinación, sin dependencia |
| `Pertenece` | Sí | Una forma parte de otra como componente, módulo o producto del mismo ecosistema. Va del hijo al padre |

---

### `catalogos`
Centraliza los valores permitidos para campos seleccionables. **Ya poblada.**

| Campo | Tipo | Descripción |
|---|---|---|
| `id` | INTEGER PK | Autoincremental |
| `tabla_dominio` | TEXT | Nombre de la tabla (ej: `herramientas`) |
| `dominio` | TEXT | Nombre del campo (ej: `tipo`) |
| `valor` | TEXT | Valor permitido |
| `descripcion` | TEXT | Descripción del valor |
| `orden` | INTEGER | Orden en desplegables |

**Dominios registrados:**

| dominio | tabla_dominio | Notas |
|---|---|---|
| `tipo` | `herramientas` | 6 valores |
| `categoria` | `herramientas` | 16 valores, JSON array |
| `plataforma` | `herramientas` | 9 valores, JSON array |
| `modelo_negocio` | `herramientas` | 8 valores, JSON array |
| `opensource` | `herramientas` | 3 valores |
| `vigencia` | `herramientas` | 4 valores |
| `tipo` | `herramienta_relaciones` | 5 valores |
| `procesado` | `herramientas_staging` | 4 valores |
| `destino` | `herramientas_staging` | 1 valor |

---

### Tablas de contenido y monetización *(pendientes de diseñar, Fase 6)*
El control de contenido y monetización se gestiona en tablas separadas del catálogo de herramientas. Esto mantiene limpia la separación entre "qué herramientas existen" y "qué contenido se ha producido sobre ellas".

La estructura prevista es:

- **`contenido`**: vinculada a `herramientas`. Contendrá campos como `url_afiliado`, estado de producción, fecha de publicación, etc.
- **Una tabla por red social** (`contenido_youtube`, `contenido_tiktok`, `contenido_instagram`...): cada plataforma tiene métricas y formatos distintos.

---

## Notas técnicas

- Las fechas se almacenan como `TEXT` en formato `YYYY-MM-DD`.
- Los booleanos (`requiere_registro`, `probada`) se almacenan como `INTEGER` (0/1).
- `categoria`, `plataforma` y `modelo_negocio` se almacenan como **JSON array** en TEXT. Usar `json_each()` para consultas sobre estos campos.
- `FOREIGN KEY` está activo. Activarlo explícitamente en cada conexión Python con `PRAGMA foreign_keys = ON`.
- La tabla `sqlite_sequence` es interna de SQLite y no debe tocarse.
- Las tablas `sqlite_stat1` y `sqlite_stat4` son generadas automáticamente por SQLite al ejecutar `ANALYZE`. No deben tocarse ni borrarse.
