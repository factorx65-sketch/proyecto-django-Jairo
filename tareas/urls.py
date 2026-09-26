from django.urls import path 
from . import views

urlpatterns = [
    path("",views.inicio,name='inicio'),
    path("crearTarea/",views.crearTarea ,name='crearTarea'),
    path("detalleTarea/<int:tarea_id>/",views.detalleTarea,name='detalleTarea'),
    path("eliminarTarea/<int:tarea_id>/",views.eliminarTarea,name='eliminarTarea')
]
