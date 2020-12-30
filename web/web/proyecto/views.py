from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from proyecto.models import EjemploMedicion
import random 

# Create your views here.

def index(request):
    return JsonResponse({})

def vista1(request):
    context = {}
    return render(request, 'proyecto/pagina1.html',context)

@csrf_exempt
def json_response(request):
    #print(f'request.POST es: {request.POST}')
    carnet = request.POST.get('carnet',None)
    nombre = request.POST.get('nombre',None)
    print(carnet,nombre)

    # data = {
    #     'parametro1' : 'valor1',
    #     'parametro2' : 10,
    #     'parametro3' : None,
    # }

    valor_prueba = random.randint(10,50)
    
    EjemploMedicion.objects.create(valor1=valor_prueba)
    temporal = list()
    temporal1 = list()

    mediciones = EjemploMedicion.objects.order_by('-created')[:5]
    mediciones1 = EjemploMedicion.objects.order_by('-created')[:5]

    for medicion in mediciones:
        temporal.append(medicion.valor1)
    for medicion1 in mediciones1:
        temporal1.append(medicion1.valor1)

    
    data = {
        'mediciones' : temporal ,
        'mediciones1' : temporal1 ,
    }

    return JsonResponse(data)