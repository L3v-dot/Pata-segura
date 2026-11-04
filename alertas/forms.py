from django import forms

class AlertaForm(forms.Form):
    tipo = forms.ChoiceField(label="Tipo de alerta", choices=[("perdida", "Mascota perdida"), ("encontrada", "Mascota encontrada")])
    descripcion = forms.CharField(label="Descripción", max_length=500, widget=forms.Textarea(attrs={"rows": 3, "placeholder": "Contá cómo es la mascota y qué sucedió"}))
    fotografia = forms.ImageField(label="Fotografía", widget=forms.ClearableFileInput(attrs={"accept": "image/jpeg,image/png,image/webp,image/gif"}))
    fecha = forms.DateField(label="Fecha", widget=forms.DateInput(attrs={"type": "date"}))
    ubicacion = forms.CharField(label="Ubicación", max_length=120, widget=forms.TextInput(attrs={"placeholder": "Ej. Plaza de Maipú, Santiago"}))
    contacto = forms.CharField(label="Medio de contacto", max_length=120, widget=forms.TextInput(attrs={"placeholder": "Teléfono o correo de contacto"}))

    def clean_fotografia(self):
        foto = self.cleaned_data["fotografia"]
        if foto.size > 5 * 1024 * 1024:
            raise forms.ValidationError("La imagen debe pesar como máximo 5 MB.")
        if foto.image.format not in {"JPEG", "PNG", "WEBP", "GIF"}:
            raise forms.ValidationError("Elegí una imagen JPEG, PNG, WebP o GIF.")
        return foto
