from django.shortcuts import render, redirect, HttpResponse
from .models import Anuncio_Trans, Contratista,Localidad,Transporte, Comentario
from .forms import AnuncioForm, ContratistaForm, ComentarioForm, LocalidadForm, TransporteForm,SearchForm
from django.contrib.auth.decorators import login_required
# Create your views here.
def index(request):
    if request.GET:
        search_form = SearchForm(request.GET)
    else:
        search_form = SearchForm()

    filtro_titulo = request.GET.get("titulo", "")
    orden_anuncio = request.GET.get("orden", None)
    param_comentarios_habilitados = request.GET.get("permitir_comentarios", None)
    param_categorias = request.GET.getlist("categoria")


    lista_anuncio = Anuncio_Trans.objects.filter(titulo__icontains = filtro_titulo)
    lista_contrato = Contratista.objects.filter(titulo__icontains = filtro_titulo)
    
    if param_comentarios_habilitados:
        anuncios = anuncios.filter(permitir_comentarios = True)
    
    if orden_anuncio == "titulo":
        anuncios= anuncios.order_by("titulo")
    elif orden_anuncio == "antiguo":
        anuncios= anuncios.order_by("fecha_creado")
    elif orden_anuncio == "nuevo":
        anuncios= anuncios.order_by("-fecha_creado")
    contexto={ 
    "lista_anuncio" : lista_anuncio,
    "lista_contrato": lista_contrato,
    "search_form":search_form,
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


@login_required
def borrar_anuncioT(request,id):
    anuncio = Anuncio_Trans.objects.get(pk=id)
    if request.method == "POST":
        if anuncio.usuario == request.user:
            anuncio.delete()
            return redirect("ver_perfil", request.user.id)

def search(request):
    return HttpResponse("hola")
    anuncio = Anuncio_Trans.objects.get(pk=id)

"""def search(request): 
    # parametros
    param_titulo = request.GET.get('titulo','')
    #param_payment = request.GET.get('param_payment','')
    #param_delivery = request.GET.get('param_delivery','')
    #param_orden =request.GET.get('param_orden','')

    # filtrar titulo
    publicaciones = Anuncio_Trans.objects.filter(titulo__contains=param_titulo)
    form = SearchForm()
    contexto = {"form":form, "publicaciones":publicaciones}

    return render(request, "anuncio/search.html", contexto)"""