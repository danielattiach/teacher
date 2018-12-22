from django.urls import path
from . import views

urlpatterns = [
  path('send/', views.send, name='send'),
  path('delete/', views.delete_message, name='delete'),
  path('reply/<int:msg_id>', views.reply_message, name='reply'),
  path('tm/', views.teacher_message, name='tm'),
  path('um/', views.user_message, name='um')
]