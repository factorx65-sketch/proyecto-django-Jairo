
from django.contrib import admin
from django.urls import path, include
from django.views.generic.base import RedirectView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('tareas/',include('tareas.urls')),
    path('',RedirectView.as_view(url='tareas/', permanent=True))
]
