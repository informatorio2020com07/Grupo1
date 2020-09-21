from django.shortcuts import render, redirect
from .models import Anuncio_Trans, Contratista,Localidad,Transporte, Comentario
from .forms import AnuncioForm, ContratistaForm, ComentarioForm, LocalidadForm, TransporteForm
from django.contrib.auth.decorators import login_required
# Create your views here.
def index(request):
    lista_anuncio = Anuncio_Trans.objects.all()[0:12]
    lista_contrato = Contratista.objects.all()[0:12]
    contexto={ 
    "lista_anuncio" : lista_anuncio,
    "lista_contrato": lista_contrato
    }
    return render(request, "anuncio/index.html", contexto)

def ver_anuncio(request,id):
    anuncio = Anuncio_Trans.objects.get(pk=id)
    usuario = anuncio.usuario
    lista_anuncio = Anuncio_Trans.objects.filter(usuario_id=usuario.id)
    form_comentario = ComentarioForm()
    comentarios = anuncio.comentario_set.all().order_by("-fecha_creacion")
    contexto = {
    "anuncio" : anuncio,
    "lista_anuncio" : lista_anuncio,
    "form_comentario": form_comentario,
    "comentarios":comentarios,
    }
    return render(request, "anuncio/ver_transportista.html",contexto)

def ver_contratista(request,id):
    anuncio = Contratista.objects.get(pk=id)
    usuario = anuncio.usuario
    lista_anuncio = Contratista.objects.filter(usuario_id=usuario.id)
    form_comentario = ComentarioForm()
    contexto = {
    "anuncio" : anuncio,
    "lista_anuncio" : lista_anuncio,
    "form_comentario": form_comentario
    }
    return render(request, "anuncio/ver_contratista.html",contexto)

#Transportista
@login_required
def nuevo_anuncio(request):
    if request.method == "POST":
        form=AnuncioForm(request.POST)
        if form.is_valid():
            anuncio=form.save(commit=False)
            anuncio.usuario = request.user
            anuncio.save()
            return redirect("ver_anuncio", anuncio.id)
        else:
            contexto={"form":form}
            return render(request, "anuncio/nuevo_anuncio.html", contexto)
    form=AnuncioForm()
    contexto={"form":form}
    return render(request, "anuncio/nuevo_anuncio.html", contexto)

#Contratista
def anuncio_nuevo(request):
    if request.method == "POST":
        form=ContratistaForm(request.POST)
        if form.is_valid():
            anuncio=form.save(commit=False)
            anuncio.usuario = request.user
            anuncio.save()
            return redirect("ver_contratista", anuncio.id)
        else:
            contexto={"form":form}
            return render(request, "anuncio/anuncio_nuevo.html", contexto)
    form=ContratistaForm()
    contexto={"form":form}
    return render(request, "anuncio/anuncio_nuevo.html", contexto)

@login_required
def comentar(request,id):
    anuncio = Anuncio_Trans.objects.get(pk=id)
    if anuncio.permitir_comentarios:
        if request.method == "POST":
            form = ComentarioForm(request.POST)
            if form.is_valid():
                comentario = form.save(commit=False)
                comentario.usuario = request.user
                comentario.anuncio = anuncio
                comentario.save()
                return redirect("ver_anuncio", anuncio.id)
    else:
        return redirect("ver_anuncio", anuncio.id)


