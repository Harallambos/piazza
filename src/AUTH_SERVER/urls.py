# AUTHORISATION SERVER URLS FILE
# ------------------------------------------------------------------------------------------------------------------
from django.conf.urls import url, include
import oauth2_provider.views as oauth2_views
from django.conf import settings

from django.urls import path
from . import views
from .views import UserRegisterView, UserEditView, PasswordsChangeView

from django.contrib.auth import views as auth_views


urlpatterns = [
    
    path('registration/', UserRegisterView.as_view(), name='registration'),
    path('edit_profile/', UserEditView.as_view(), name='edit_profile'),
    path('password/', PasswordsChangeView.as_view(template_name='registration/change-password.html')),
    path('password_success', views.password_success, name="password_success"),


    path('register/', views.register), 
    path('token/', views.token), 
    path('token/refresh/', views.refresh_token), 
    path('token/revoke/', views.revoke_token),
]