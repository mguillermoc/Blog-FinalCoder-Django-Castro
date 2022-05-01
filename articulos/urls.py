from django.urls import path
from . import views

urlpatterns = [
    path('', views.ArticuloList.as_view(), name='List'),
    path('nuevo/', views.creararticulo.as_view(), name='New'),
    path('<pk>/', views.ArticuloDetalle.as_view(), name='Detail'),
    path('editar/<pk>/', views.modarticulo.as_view(), name='art_Edit'),
    path('borrar/<pk>/', views.deletearticulo.as_view(), name='art_Delete'),
]
