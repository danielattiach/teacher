from django.urls import path

from . import views

urlpatterns = [
    path('login', views.login, name='login'),
    path('register', views.register, name='register'),
    path('logout', views.logout, name='logout'),
    path('dashboard', views.dashboard, name='dashboard'),
    path('message/<int:message_id>', views.message, name="message"),
    path('upload/', views.upload_avatar, name="upload_avatar")
]