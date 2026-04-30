# ==============================================================
# GenerarEstructura.ps1
# AppDex - Generador de árbol de estructura del proyecto
#
# Lee la configuración desde config.ini en la raíz del proyecto.
# ==============================================================


# --- FUNCIÓN: Leer config.ini ---
function Read-Config {
    param ([string]$RutaIni)

    $config = @{}
    $seccion = ""

    foreach ($linea in Get-Content $RutaIni -Encoding UTF8) {
        $linea = $linea.Trim()

        # Ignorar comentarios y líneas vacías
        if ($linea -eq "" -or $linea.StartsWith("#")) { continue }

        # Detectar sección
        if ($linea -match "^\[(.+)\]$") {
            $seccion = $matches[1].Trim()
            continue
        }

        # Leer clave = valor
        if ($linea -match "^(.+?)\s*=\s*(.*)$") {
            $clave = "$seccion.$($matches[1].Trim())"
            $valor = $matches[2].Trim()
            $config[$clave] = $valor
        }
    }
    return $config
}


# --- CARGAR CONFIGURACIÓN ---
# Buscamos config.ini en la carpeta padre de Scripts\Otros (es decir, la raíz del proyecto)
$RutaScript  = Split-Path -Parent $MyInvocation.MyCommand.Path
$RutaRaiz    = Split-Path -Parent (Split-Path -Parent $RutaScript)
$RutaIni     = Join-Path $RutaRaiz "config.ini"

if (-not (Test-Path $RutaIni)) {
    Write-Host "No se encontro config.ini en: $RutaIni" -ForegroundColor Red
    exit 1
}

$config = Read-Config -RutaIni $RutaIni

$RutaProyecto  = $config["rutas.proyecto"]
$ArchivoSalida = $config["rutas.estructura_md"]
$IgnorarRaw    = $config["configuracion.ignorar_estructura"]
$Ignorar       = $IgnorarRaw -split "," | ForEach-Object { $_.Trim().ToLower() }


# --- LÓGICA: Generar árbol de texto ---
function Get-ArbolTexto {
    param (
        [string]$Path,
        [string]$Prefix = ""
    )

    $Resultado = ""
    $Items = @(Get-ChildItem -Path $Path -Force -ErrorAction SilentlyContinue |
               Where-Object { $Ignorar -notcontains $_.Name.ToLower() })

    $Count = $Items.Count
    for ($i = 0; $i -lt $Count; $i++) {
        $Item    = $Items[$i]
        $EsUltimo = ($i -eq $Count - 1)

        $Conector = if ($EsUltimo) { "\--- " } else { "+--- " }
        $Resultado += "$Prefix$Conector$($Item.Name)`r`n"

        if ($Item.PSIsContainer) {
            $NuevoPrefix = if ($EsUltimo) { $Prefix + "    " } else { $Prefix + "|   " }
            $Resultado += Get-ArbolTexto -Path $Item.FullName -Prefix $NuevoPrefix
        }
    }
    return $Resultado
}


# --- EJECUCIÓN ---
if (Test-Path $RutaProyecto) {
    Write-Host "Generando estructura..." -ForegroundColor Cyan

    $NombreRaiz  = (Get-Item $RutaProyecto).Name
    $CuerpoArbol = Get-ArbolTexto -Path $RutaProyecto

    $MarkdownLines = @()
    $MarkdownLines += "# Estructura del Proyecto"
    $MarkdownLines += "Actualizado: $(Get-Date -Format 'yyyy-MM-dd HH:mm:ss')"
    $MarkdownLines += ""
    $MarkdownLines += '```text'
    $MarkdownLines += $NombreRaiz
    $MarkdownLines += $CuerpoArbol.TrimEnd("`r`n")
    $MarkdownLines += '```'

    $MarkdownLines | Out-File -FilePath $ArchivoSalida -Encoding utf8

    Write-Host "Listo! Arbol guardado en: $ArchivoSalida" -ForegroundColor Green
} else {
    Write-Host "La ruta del proyecto no existe: $RutaProyecto" -ForegroundColor Red
    exit 1
}
