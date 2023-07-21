from django.shortcuts import render, redirect
from .forms import NoticiaForm, Noticia
from .models import Noticia

def index(request):
    return render(request,'index.html',)

# views.py
def crear_noticia(request):
    if request.method == 'POST':
        form = NoticiaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('nombre_de_la_url_de_lista_de_noticias')  # Redirige a la lista de noticias
    else:
        form = NoticiaForm()

    return render(request, 'crear_noticia.html', {'form': form})


def lista_noticias(request):
    noticias = Noticia.objects.all().order_by('-fecha_publicacion')
    return render(request, 'lista_noticias.html', {'noticias': noticias})

def editar_noticia(request, noticia_id):
    noticia = get_object_or_404(Noticia, pk=noticia_id)

    if request.method == 'POST':
        form = NoticiaForm(request.POST, instance=noticia)
        if form.is_valid():
            form.save()
            return redirect('noticias')
    else:
        form = NoticiaForm(instance=noticia)

    return render(request, 'editar_noticia.html', {'form': form})

def eliminar_noticia(request, noticia_id):
    noticia = get_object_or_404(Noticia, pk=noticia_id)

    if request.method == 'POST':
        noticia.delete()
        return redirect('noticias')
    
    return render(request, 'eliminar_noticia.html', {'noticia': noticia})






