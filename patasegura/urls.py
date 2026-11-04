from django.urls import path
from alertas import views
urlpatterns = [path("", views.inicio, name="inicio")]
