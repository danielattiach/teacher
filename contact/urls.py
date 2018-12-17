from django.urls import path
from . import views

urlpatterns = [
  path('send/', views.send, name='send'),
  path('delete/', views.delete_message, name='delete'),
  path('pm/<int:msg_id>', views.private_message, name='pm')
]