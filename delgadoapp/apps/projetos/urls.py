from django.urls import path
from . import views

app_name = 'projetos'

urlpatterns = [
    path('', views.lista_projetos, name='lista_projetos'),
    path('adicionar/', views.adiciona_projetos, name='adiciona_projetos'),
    path('editar/<int:id_projeto>/', views.edit_projetos, name='edit_projetos'),
    path('excluir/<int:id_projeto>/', views.delete_projetos, name='delete_projetos'),
]