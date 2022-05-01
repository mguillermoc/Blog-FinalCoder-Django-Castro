from django.shortcuts import render, redirect
from chat.models import sala, mensaje
from django.http import HttpResponse, JsonResponse
from django.contrib.auth.decorators import login_required


# Create your views here.

@login_required
def chat(request):
    return render(request,'chat.html')

def salas(request,Sala):
    Username = request.GET.get('usuario')
    Detalle_Sala = sala.objects.get(name=Sala)
    return render(request,'sala.html', {
        'usuario': Username,
        'sala': Sala,
        'Detalle_Sala' : Detalle_Sala
    })

@login_required
def revision(request):
    Sala = request.POST['nombre_sala']
    Username = request.POST['usuario']
    if sala.objects.filter(nombre=Sala) is not None:
        return redirect('/'+Sala+'/?usuario='+Username)
    else:
        nueva_sala= sala.objects.create(nombre=Sala)
        nueva_sala.save
        return redirect('/'+Sala+'/?usuario='+Username)

@login_required
def enviado(request):
    Mensaje = request.POST['mensaje']
    Username = request.POST['usuario']
    sala_id = request.POST['sala_id']
    nuevo_mensaje = mensaje.objects.create(value=Mensaje, usuario=Username, sala=sala_id)
    nuevo_mensaje.save()
    return HttpResponse('Mensaje enviado con éxito')
    
@login_required
def getmensajes(request, Sala):
    sala_detalles = sala.objects.get(nombre=Sala)
    Mensajes = mensaje.objects.filter(sala=sala_detalles.id)
    return JsonResponse({'mensaje':list(mensaje.values())})