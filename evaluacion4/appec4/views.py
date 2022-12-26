from django.shortcuts import render, HttpResponse

# Create your views here.
def inicio(request):
    return render(request,'inicio.html')

def listar_cursos(request):
    mensaje=f'''
    <h1>Listado de Cursos</h1>
    '''
    return HttpResponse(mensaje)

def crear_curso(request):
    mensaje='''
    <h1>Agregar Curso</h1>
    '''
    return HttpResponse(mensaje)

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

