"""delgadoapp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('core.urls', namespace='core')),
    path('categorias/', include('categories.urls', namespace='categories')),
    path('generos/', include('generos.urls', namespace='generos')),
    path('pagamentos/', include('pagamentos.urls', namespace='pagamentos')),
    path('funcionarios/', include('funcionarios.urls', namespace='funcionarios')),
    path('projetos/', include('projetos.urls', namespace='projetos')),
    path('contas/', include('accounts.urls', namespace='accounts')),

]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

