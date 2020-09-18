"""Loquepinte URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.urls import path, include
# aca importamos las vistas creadas de la app
from apps.restaurantes import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('principal/', views.principal, name='principal'),
    path('restaurante/', views.restaurante, name='restaurante'),
    path('el_patron/', views.el_patron, name='el_patron'),
    path('el_surtidor/', views.el_surtidor, name='el_surtidor'),
    path('la_chimenea/', views.la_chimenea, name='la_chimenea'),
    path('nanas/', views.nanas, name='nanas'),
    path('san_jose/', views.san_jose, name='san_jose'),
    path('contactar/', views.contactar, name='contactar'),
    path('accounts/', include('django.contrib.auth.urls' )), # esto trae la ruta del login, la del log out, etc
    path('registrar/', views.registro_usuario, name='registro_usuario'),
    path('error/', views.error, name='error'),
    path('comentario/', views.comentario, name='comentario'),
    path('comentarios/', views.comentarios, name='comentarios'),       
 # Password reset links (ref: https://github.com/django/django/blob/master/django/contrib/auth/views.py)
    path('password_change/done/', auth_views.PasswordChangeDoneView.as_view(template_name='registration/password_change_done.html'), 
        name='password_change_done'),

    path('password_change/', auth_views.PasswordChangeView.as_view(template_name='registration/password_change.html'), 
        name='password_change'),

    path('password_reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='registration/password_reset_done.html'),
     name='password_reset_done'),

    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='registration/password_reset_complete.html'),
     name='password_reset_complete'),
]
