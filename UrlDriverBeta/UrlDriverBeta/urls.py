"""
URL configuration for UrlDriverBeta project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.contrib.auth import views as auth_views
from django.urls import path, include
from core.views import user_login, user_logout, sign_up

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', user_login, name='login'),
    path('logout/', user_logout, name='logout'),
    path('signup/', sign_up, name='signup'),
    # Página para solicitar redefinição de senha
    path('password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),

    # Página informando que o e-mail foi enviado
    path('password_reset_done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),

    # Página para inserir a nova senha
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),

    # Página de sucesso após redefinição da senha
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
    path('', include('FileManagement.urls')),
]