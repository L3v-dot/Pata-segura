@echo off
cd /d "%~dp0"
if not exist ".venv\Scripts\python.exe" (
  echo No se encontro el entorno .venv. Segui las instrucciones del README.
  pause
  exit /b 1
)
echo Abri http://127.0.0.1:8000/ en tu navegador.
echo Para detener la aplicacion, presiona Ctrl+C.
.venv\Scripts\python.exe manage.py runserver --noreload
pause
