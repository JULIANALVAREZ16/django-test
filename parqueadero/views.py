from django.db import IntegrityError
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
from random import randrange

# Create your views here.
from django.http import HttpResponse
from .models import  Usuario, Punto, Parkine

from .forms import inicioForm, usuariosForm


def index(request):
    return HttpResponse(":::Welcom to my site:::")


def lista_usurio(request):
    # return HttpResponse ("Here you find a list of users")
    usuarios = Usuario.objects.all()
    return render(request, 'parqueadero/user.html', {'usuario': usuarios})


def loguin(request):
    form = inicioForm()
    if request.method == "POST":
        form = inicioForm(request.POST)
        if form.is_valid():
            try:
                user = authenticate(
                    request, username=form.cleaned_data['email'], password=form.cleaned_data['password'])
                if user is None:
                    print('hola login')
                    
                    error_messages = "correo o contraseña incorrectos."
                    
                    return render(request, 'parqueadero/login.html', {'form': form, 'error_messages': error_messages})

                login(request, user)

                return redirect('home')

            except IntegrityError:
                print('lola')
                # error_message = "correo o contraseña incorrectos."
                # return render(request, 'parqueadero/home.html', {'form': form, 'error_message': error_message})

    return render(request, 'parqueadero/login.html', {'form': form})


def register(request):
    form = usuariosForm()
    if request.method == "POST":
        form = usuariosForm(request.POST)
        if form.is_valid():
            # form.cleaned_data['password']
            try:
                usuario_nuevo = Usuario()

                usuario_nuevo.nombre = form.cleaned_data['nombre']
                usuario_nuevo.apellido = form.cleaned_data['apellido']
                usuario_nuevo.código = form.cleaned_data['codigo']
                usuario_nuevo.identificación = form.cleaned_data['identificacion']
                usuario_nuevo.password = form.cleaned_data['password']
                usuario_nuevo.email = form.cleaned_data['email']
                usuario_nuevo.id_programas = form.cleaned_data['id_programa']

                usuario_nuevo.save()
                user = User.objects.create_user(
                    form.cleaned_data['email'], password=form.cleaned_data['password'])
                user.save()
                login(request, user) 
                return redirect('home')


            except IntegrityError:

                error_message = "Ya existe un usuario registrado con este correo electrónico."
                return render(request, 'parqueadero/register.html', {'form': form, 'error_message': error_message})

    return render(request, 'parqueadero/register.html', {'form': form})


def home(request):

    return render(request, 'parqueadero/home.html')

    # if estoy logeado me quedo
    # else redirecciono al loginS


def points(request):
    puntos = Punto.objects.all()
    return render(request, 'parqueadero/puntos.html', {'punto': puntos})


def headquarters(request):
    return render(request, 'parqueadero/sedes.html')

def season_cen(request):
    return render(request, 'parqueadero/estaciones/estacion_cen.html')

def season_dam(request):
    return render(request, 'parqueadero/estaciones/estacion_dam.html')

def cen_estacion_a(request):
    puntos = Punto.objects.filter(id_estacion="cen_a");
    return render(request, 'parqueadero/estaciones/cen/punto_a.html', {"puntos": puntos})

def cen_estacion_otros(request, slug):
    return render(request, 'parqueadero/estaciones/cen/punto_otros.html', {'estacion': slug})

def dam_estacion_otros(request, slug):
    return render(request, 'parqueadero/estaciones/cen/punto_otros.html', {'estacion': slug})

@login_required
def my_account(request):
    user = Usuario.objects.get(email__exact=request.user.username)

    try:
        parkine = Parkine.objects.get(id_usurio = user)
    except Parkine.DoesNotExist:
        parkine = None

    return render(request, 'parqueadero/mi_cuenta.html', {'usuario': user, 'parkine': parkine})


def base(request):
    return render(request, 'parqueadero\base.html')

@login_required
def cerrar_sesion(request):
    logout(request)
    return redirect('home')

@login_required
def punto(request, id):

    if (request.method == "POST"):

        usuario = Usuario.objects.get(email__exact=request.user.username)

        try:
            parkine = Parkine.objects.get(id_usurio = usuario)
        except Parkine.DoesNotExist:
            parkine = None
        
        if (parkine != None):
            return render(request, 'parqueadero/parkine_error.html')

        list = ["1", "2", "4", "5","7", "8", "9", "0", "A", "B", "C", "D"]
        password = ""

        while (len(password) != 6):
            password = password + list[randrange(len(list))]
        
        punto = Punto.objects.get(id_punto = id)

        parkine = Parkine()
        parkine.id_punto = punto
        parkine.id_usurio = usuario
        parkine.password = password
        parkine.save()

        punto.estado = False
        punto.save()


        return render(request, 'parqueadero/parkine.html', {'punto': punto, 'parkine': parkine})
    else:
        punto = Punto.objects.get(id_punto = id)

        if (punto.estado == False):
            return render(request, 'parqueadero/ocupado.html', {'punto': punto})

        return render(request, 'parqueadero/punto.html', {'punto': punto})

def validar_punto(request, id, password):
    try:
        punto = Punto.objects.get(id_punto = id)

        parkine = Parkine.objects.get(id_punto = punto)

        if(password == parkine.password):
            return HttpResponse(status=200)

        return HttpResponse(status=400)

    except:
        return HttpResponse(status=400)

def liberar(request, id):
    try:
        punto = Punto.objects.get(id_punto = id)
        punto.estado = True
        punto.save()
        
        Parkine.objects.filter(id_punto = punto).delete()

        return HttpResponse(status=200)

    except:
        return HttpResponse(status=400)