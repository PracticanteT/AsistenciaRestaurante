"""
URL configuration for AsistenciaRestaurante project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
# Importación de módulos necesarios para configurar las URLs
from django.contrib import admin  # Permite acceder a la interfaz de administración de Django
from django.urls import path, include  # Funciones para definir patrones de URL y para incluir otras configuraciones de URL
from django.contrib.auth import views as auth_views  # Vistas genéricas para autenticación proporcionadas por Django
from django.views.generic.base import RedirectView  # Vista para redireccionar URL

# Definición de los patrones de URL para la aplicación
urlpatterns = [
    # Ruta para la interfaz de administración de Django
    path('admin/', admin.site.urls),

    # Ruta para incluir las URLs del app 'ControlAsistencia'. Esto se refiere a otro archivo urls.py dentro de ese app.
    path('asistencia/', include('ControlAsistencia.urls')),

    # Ruta para la página de inicio de sesión, utilizando una vista genérica de Django
    # Se especifica un template personalizado para el login.
    path('login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),

    # Ruta para la página de cierre de sesión
    # Se redirige al usuario a la página de login después de cerrar sesión.
    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),

    # Ruta para incluir todas las URLs de autenticación predeterminadas de Django, como el cambio de contraseña
    path('', include('django.contrib.auth.urls')),
]
