from django.urls import path
from . import views

urlpatterns = [
    path('', views.ArticuloList.as_view(), name='List'),
    path('<pk>/', views.ArticuloDetalle.as_view(), name='Detail'),
    path('nuevo', views.creararticulo.as_view(), name='New'),
    path('editar', views.modarticulo.as_view(), name='Edit'),
    path('borrar', views.deletearticulo.as_view(), name='Delete'),
]
