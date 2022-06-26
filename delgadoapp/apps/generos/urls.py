from django.urls import path
from . import views

app_name = 'generos'

urlpatterns = [
    path('', views.lista_generos, name='lista_generos'),
    path('adicionar/', views.adiciona_generos, name='adiciona_generos'),
    path('editar/<int:id_genero>/', views.edit_generos, name='edit_generos'),
    path('excluir/<int:id_genero>/', views.delete_generos, name='delete_generos'),
]