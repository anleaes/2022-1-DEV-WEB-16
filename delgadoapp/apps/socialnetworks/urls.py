from django.urls import path
from . import views

app_name = 'projetos'

urlpatterns = [
    path('', views.lista_projetos, name='lista_projetos'),
    path('adicionar/', views.adiciona_projetos, name='adiciona_projetos'),
    path('editar/<int:id_socialnetwork>/', views.edit_socialnetwork, name='edit_socialnetwork'),
    path('excluir/<int:id_socialnetwork>/', views.delete_socialnetwork, name='delete_socialnetwork'),
]