from django.contrib.auth import views as auth_views
from django.urls import path

from . import views

urlpatterns = [
    # our custom login
    # path('login/', views.user_login, name='login'),

    # using django auth views
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),

    path('', views.dashboard, name='dashboard'),
]
