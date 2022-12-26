from django.shortcuts import render, HttpResponse,redirect
from appec4.models import Course
from django.contrib import messages


# Create your views here.
def inicio(request):
    return render(request,'inicio.html')
def ruta_curso(request):
    return render(request,'agregar_cursos.html')

def listar_cursos(request):
    cursos= Course.objects.all()
    return render(request,'listar_cursos.html',{
        'titulo':'Lista de Cursos',
        'cursos': cursos
    })


def crear_curso(request):
    if request.method == 'POST':
        creditos= request.POST ['creditos']
        nombre=request.POST ['nombre']
        horas=request.POST['horas']
        codigo=request.POST['codigo']
        estado=request.POST['estado']
    
    curso= Course(
        code=codigo,
        name=nombre,
        hour=horas,
        credits=creditos,
        state=estado
    )
    curso.save()

    messages.success(request,f"Se Agrego Correctamente")
    return redirect('listar_cursos.html')
    

def carreras(request):
    mensaje='''
    <h1>Listado de Carreras</h1>
    '''
    return HttpResponse(mensaje)

def crear_carrera(request):
    mensaje='''
    <h1>Agregar Carreras</h1>
    '''
    return HttpResponse(mensaje)

