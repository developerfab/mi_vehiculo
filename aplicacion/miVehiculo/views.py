from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

from miVehiculo.models import *
from utils import *

# Create your views here.

def index(request):
	contexto = {}
	return render(request, 'index.html', contexto)

def loginView(request):
	"""
	login del usuario
	"""
	contexto = {}
	username = request.POST['username']
	password = request.POST['password']
	user = authenticate(username=username, password=password)
	if user is not None:
		if user.is_active:
			login(request, user)
			contexto={'username':username}
		else:
			contexto['mensaje'] = "usuario no activo"
			return render(request, 'index.html', contexto)
	else:
		contexto['mensaje'] = 'Error en los datos, por favor revise'
		user = None
		return render(request, 'index.html', contexto)
	return redirect('../home/')

@login_required
def logoutView(request):
    """
    Logout del usuario con sesion iniciada
    """
    contexto={'mensaje':'Salida exitosa'}
    logout(request)
    return render(request, 'index.html', contexto)

@login_required
def home(request):
    """
    Vista principal del usuario logeado
    """
    contexto={'perfil':True}
    usuario = Usuario.objects.get(username=request.user.username)
    tipoLicencia = usuario.tipo_licencia
    nombre = usuario.first_name
    documento = usuario.documento
    #consola de lista de vehiculos del usuario
    vehiculos = Vehiculo.objects.filter(propietario=usuario)
    fecha = fechaLicencia(usuario.fecha_licencia, tipoLicencia)
    contexto['nombre'] = nombre
    contexto['documento'] = documento
    contexto['tipoLicencia'] = tipoLicencia
    contexto['vehiculos'] = vehiculos
    return render(request, 'perfil.html', contexto)

@login_required
def misImpuestos(request):
    """
    Vista principal para la visualizacion de los impuestos de un vehiculo
    """
    contexto={'perfil':False}
    usuario = Usuario.objects.get(username=request.user.username)
    tipoLicencia = usuario.tipo_licencia
    #se llama el modulo para calcular la fecha de expiracion de la licencia
    fecha = fechaLicencia(usuario.fecha_licencia, tipoLicencia)
    contexto['fecha']=fecha
    return render(request, 'impuesto.html', contexto)

