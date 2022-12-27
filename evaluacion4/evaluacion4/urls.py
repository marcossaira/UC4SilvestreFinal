"""evaluacion4 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from appec4 import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.inicio,name='inicio'),
    path('listar_carreras/', views.listar_carreras, name='listar_carreras'),
    path('agregar_carreras/', views.crear_carrera, name='agregar_carreras'),
    path('ruta_cursos/', views.ruta_cursos, name='ruta_cursos'),
    path('ruta_carreras/', views.ruta_carreras, name='ruta_carreras'),
    path('listar_cursos/', views.listar_cursos, name='listar_cursos'),
    path('agregar_cursos/', views.crear_curso, name='agregar_cursos'),

    path('eliminar_curso/<int:id>', views.eliminar_curso, name='eliminar_curso'),
    path('eliminar_carrera/<int:id>', views.eliminar_carrera, name='eliminar_carrera'),
  
]
