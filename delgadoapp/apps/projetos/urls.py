from django.urls import path
from . import views

app_name = 'projetos'

urlpatterns = [
    path('', views.list_projetos, name='list_projetos'),
    path('excluir-item/<int:id_projeto>/', views.delete_projeto, name='delete_projeto'),
    path('adicionar-item/', views.add_projeto, name='add_projeto'),
    path('editar-status/<int:id_projeto>/', views.edit_projeto, name='edit_projeto'),
]
