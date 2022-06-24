from django.urls import path
from . import views

app_name = 'orders'

urlpatterns = [
    path('', views.list_orders, name='list_orders'),
    path('excluir-item/<int:id_order_item>/', views.delete_order_item, name='delete_order_item'),
    path('adicionar-item/', views.add_order_item, name='add_order_item'),
    path('editar-status/<int:id_order>/', views.edit_order_status, name='edit_order_status'),
]
