@echo off
echo Instalando dependencias...
pip install -r "%~dp0requirements.txt" --quiet

echo.
echo Arrancando AppDex Dashboard...
echo Accede desde el navegador en: http://localhost:5000
echo Para acceder desde movil usa la IP de este PC en la misma red WiFi.
echo.
echo Pulsa Ctrl+C para parar el servidor.
echo.

python "%~dp0app.py"
pause
