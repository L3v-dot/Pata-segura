import base64
from datetime import date
from django.shortcuts import redirect, render
from .forms import AlertaForm

# Esta lista vive solo en la memoria del proceso de desarrollo.
ALERTAS = [{"tipo": "perdida", "descripcion": "Perrito café con collar. Se perdió cerca de la plaza.", "fotografia": "perro", "fecha": date(2026, 11, 2), "ubicacion": "Maipú, Santiago", "contacto": "contacto@example.com", "ejemplo": True}]

def inicio(request):
    formulario = AlertaForm(request.POST or None, request.FILES or None)
    if request.method == "POST" and formulario.is_valid():
        alerta = formulario.cleaned_data.copy()
        foto = alerta.pop("fotografia")
        formato = foto.image.format.lower()
        contenido = base64.b64encode(foto.read()).decode("ascii")
        alerta["foto_url"] = f"data:image/{formato};base64,{contenido}"
        ALERTAS.insert(0, alerta)
        return redirect("inicio")
    alertas = sorted(ALERTAS, key=lambda alerta: alerta["fecha"], reverse=True)
    return render(request, "alertas/inicio.html", {"formulario": formulario, "alertas": alertas})
