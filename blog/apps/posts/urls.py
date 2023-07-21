from django.contrib import admin
from django.urls import path, include
from .views import index, crear_noticia, lista_noticias, editar_noticia


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('', include('apps.posts.urls')),
    path('crear_noticia/',crear_noticia, name='crear_noticia'),
    path('', include('apps.urls')),
    path('noticias/', lista_noticias, name='lista_noticias'),
    path('editar_noticia/<int:noticia_id>/', editar_noticia, name='editar_noticia'),
    
]