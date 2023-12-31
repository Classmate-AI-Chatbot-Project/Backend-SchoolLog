# chat/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('<str:user_id>/<int:chatroom_id>/', views.chat_service, name='chatbot'),
    path('result/<str:user_id>/<int:chatroom_id>/', views.chat_result, name='chatResult'),
]

