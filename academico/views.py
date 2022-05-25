from django.shortcuts import render,redirect
from .models import Curso, Familiar

# Create your views here.
def home(request):
    cursos = Curso.objects.all() #Retorna el listado de todos los cursos
    return render(request,"gestionCursos.html",{"cursos":cursos})

def registrarCurso(request):
    #Recibe los datos del form y los guarda en variables
    codigo=request.POST['txtCodigo']
    nombre=request.POST['txtNombre']
    creditos=request.POST['numCreditos']

    curso = Curso.objects.create(codigo=codigo,nombre=nombre,creditos=creditos) #creo un nuevo objeto con los parametros que obtuve del formulario

    return redirect('/')


def eliminarCurso(request,codigo):
    curso=Curso.objects.get(codigo=codigo)#Solicita a la bd el curso cuyo codigo coincida con el codigo pasado por parametro en la url
    curso.delete() 
    return redirect('/')

def edicionCurso(request,codigo):
    curso=Curso.objects.get(codigo=codigo)
    return render(request,"edicionCurso.html",{"curso":curso})

def editarCurso(request):
    codigo=request.POST['txtCodigo']
    nombre=request.POST['txtNombre']
    creditos=request.POST['numCreditos']

    curso=Curso.objects.get(codigo=codigo)

    #Reasigno los valores
    curso.nombre = nombre
    curso.codigo=codigo
    curso.creditos=creditos

    curso.save() #Para guardar los nuevos datos

    return redirect('/')