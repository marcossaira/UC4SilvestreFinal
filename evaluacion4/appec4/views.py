from django.shortcuts import render, HttpResponse,redirect
from appec4.models import Course,Career
from django.contrib import messages

# Create your views here.
def inicio(request):
    return render(request,'inicio.html')

def ruta_cursos(request):
    return render(request,'agregar_cursos.html')

def ruta_carreras(request):
    return render(request,'agregar_carrera.html')

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

    messages.success(request,f"Se agrego el curso Correctamente")
    return redirect('inicio')
    

def listar_carreras(request):
    carreras= Career.objects.all()
    return render(request,'listar_carrera.html',{
        'titulo':'Lista de Carrera',
        'carreras': carreras
    })

def crear_carrera(request):
    if request.method == 'POST':
        nombre= request.POST ['nombre']
        siglas=request.POST ['siglas']
        descripcion=request.POST['descripcion']
        estado=request.POST['estado']
        imagen=request.POST['imagen']
        carreras= Career(
        name=nombre,
        shortname=siglas,
        description=descripcion,
        state=estado,
        imagen=imagen
    )
    
    carreras.save()
    messages.success(request,f"Se creo la carrera correctamente")
    return redirect('inicio')

def eliminar_carrera(request,id):
    carrera=Career.objects.get(pk=id)
    carrera.delete()
    return render(request,'inicio.html')

def eliminar_curso(request,id):
    curso=Course.objects.get(pk=id)
    curso.delete()
    return render(request,'inicio.html')

