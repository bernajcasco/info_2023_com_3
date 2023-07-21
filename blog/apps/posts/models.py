from django.db import models
from django.utils import timezone

# Create your models here.



#categoria
class Categoria(models.Model):
    nombre = models.CharField(max_length=200, null=False)
    activo = models.BooleanField(default=True)
    creacion = models.DateTimeField(auto_now_add=True)
    actualizacion = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['nombre']

    def __str__(self):
        return self.nombre
    
    
class Post(models.Model):
    titulo = models.CharField(max_length=50, null=False)
    subtitulo = models.CharField(max_length=100, null=True, blank=True)
    fecha = models.DateTimeField(auto_now_add=True)
    texto = models.TextField(null=False)
    activo = models.BooleanField(default=True)
    categoria = models.ForeignKey(Categoria, on_delete=models.SET_NULL,null=True,default='sin categoria')
    imagen = models.ImageField(null=True, blank=True, upload_to='media',default='static/post_default.png')
    publicado = models.DateTimeField(default=timezone.now)
    
    class Meta:
        ordering = ('-publicado',)
    def __str__(self):
        return self.titulo
    
    def delete(self,using = None, keep_parents = False):
        self.imagen.delete(self.imagen.name)
        super().delete()

class Etiqueta(models.Model):
    nombre = models.CharField(max_length=200, unique=True)
    activo = models.BooleanField(default=True)
    creacion = models.DateTimeField(auto_now_add=True)
    actualizacion = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['nombre']

    def __str__(self):
        return self.nombre
    
class Noticia:
    def __init__(self, titulo, contenido, autor):
        self.titulo = titulo
        self.contenido = contenido
        self.autor = autor

class NoticiasManager:
    def __init__(self):
        self.noticias = []

    def crear_noticia(self, titulo, contenido, autor):
        noticia = Noticia(titulo, contenido, autor)
        self.noticias.append(noticia)

    def mostrar_lista_de_noticias(self):
        if not self.noticias:
            print("No hay noticias disponibles.")
        else:
            for i, noticia in enumerate(self.noticias, 1):
                print(f"{i}. Título: {noticia.titulo}")
                print(f"Autor: {noticia.autor}")
                print(f"Contenido: {noticia.contenido}\n")

    def editar_noticia(self, indice, titulo, contenido, autor):
        if 1 <= indice <= len(self.noticias):
            noticia = self.noticias[indice - 1]
            noticia.titulo = titulo
            noticia.contenido = contenido
            noticia.autor = autor
            print("Noticia editada correctamente.")
        else:
            print("Índice de noticia inválido.")

    def eliminar_noticia(self, indice):
        if 1 <= indice <= len(self.noticias):
            del self.noticias[indice - 1]
            print("Noticia eliminada correctamente.")
        else:
            print("Índice de noticia inválido.")