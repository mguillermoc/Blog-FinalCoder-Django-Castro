from re import U
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import Template, Context, loader
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UserChangeForm 
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required

def inicio(request):
    plantilla=loader.get_template('page.html')
    documento=plantilla.render()
    return HttpResponse(documento)

def about(request):
    plantilla=loader.get_template('about.html')
    documentos=plantilla.render()
    return HttpResponse(documentos)

def login_request(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data =request.POST)
        if form.is_valid():
            usuario = form.cleaned_data.get('username')
            contra = form.cleaned_data.get('password')
            user=authenticate(username=usuario, password=contra)

            if user is not None:
                login(request, user)
                return render(request, 'page.html', {'mensaje':f'bienvenido {usuario}'} )
            else:
                return render(request, 'page.html', {'mensaje':'Error datos incorrectos'} )
        else:
            return render(request, 'page.html', {'mensaje':'Error de formulario'} )

    form = AuthenticationForm(request, data =request.POST)
    return render(request, "login.html", {'form':form})

def register(request):
    if request.method =='POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            form.save()
            return render(request, 'page.html', {'mensaje':'Usuario creado'})
    else:
        form = UserCreationForm()
    return render(request, 'registro.html', {'form':form})

@login_required
def editarperfil(request):
    usuario = request.user
    if request.method == 'POST':
        miFormulario = UserChangeForm(request.POST)
        if miFormulario.is_valid:
            informacion = miFormulario.cleaned_data
            usuario.email = informacion['email']
            usuario.password1 = informacion['pasword1']
            usuario.password2 = informacion['pasword2']
            usuario.save()

            return render(request, 'page.htm')
    else: 
        miFormulario= UserChangeForm(initial={'email':usuario.email})
    return render(request, 'editarperfil.html', {'miFormulario': miFormulario, 'usuario' : usuario})

