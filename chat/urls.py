from django.urls import path
from . import views

urlpatterns = [
    path('', views.chat, name='chat'),
    path('<str:sala>/', views.salas, name='salas'),
    path('revision', views.revision, name='revision'),
    path('enviado', views.enviado, name='enviado'),
    path('getmensajes/<str:sala>/', views.getmensajes, name='getmensajes'),
]
