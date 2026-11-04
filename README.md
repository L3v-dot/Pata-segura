# PataSegura

Prototipo académico en Django para crear y consultar alertas de mascotas perdidas o encontradas.

## Requisitos

- Python 3.10 o superior y acceso a internet para instalar Django.

## Inicio rápido en esta computadora

El entorno `.venv` ya está preparado en esta computadora. Hacé doble clic en `Iniciar PataSegura.cmd` y abrí http://127.0.0.1:8000/ en tu navegador. Si copiás el proyecto a otra computadora, seguí los pasos de instalación de abajo.

## Inicio en Windows (PowerShell)

Abrí PowerShell en la carpeta del proyecto y ejecutá:

```powershell
py -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
python manage.py runserver --noreload
```

Si PowerShell no permite activar el entorno, podés usar directamente `.\.venv\Scripts\python.exe` en lugar de `python` en los dos últimos comandos. Abrí http://127.0.0.1:8000/ y dejá esa consola abierta. Para detener el servidor, presioná Ctrl+C.

En macOS o Linux: `python3 -m venv .venv`, `source .venv/bin/activate`, `pip install -r requirements.txt` y `python manage.py runserver --noreload`.

## Cómo probar

1. Completá el formulario con una alerta de mascota perdida, una fecha, ubicación y contacto; subí una fotografía propia (JPEG, PNG, WebP o GIF, hasta 5 MB) y pulsá **Publicar alerta**. La alerta aparece en la lista, ordenada por fecha.
2. Elegí mascota encontrada y completá los campos excepto ubicación. Al publicar, aparece un mensaje de validación y la alerta no se crea.

La imagen y la alerta precargada son ficticias. La foto fue generada con IA. Las alertas agregadas y sus fotografías se guardan solo en la memoria del proceso y se pierden al reiniciar el servidor. El prototipo usa un único proceso local; no está preparado para publicación en internet ni para guardar información real de contacto. No requiere base de datos ni migraciones.

## Cómo funciona

`alertas/forms.py` define los campos y sus validaciones. En `alertas/views.py`, la función `inicio` recibe el formulario, valida sus datos, guarda temporalmente la alerta y muestra la lista ordenada por fecha. La plantilla `alertas/templates/alertas/inicio.html` muestra el formulario, errores y resultados. La función `inicio` es un fragmento breve que se puede explicar en el video.
