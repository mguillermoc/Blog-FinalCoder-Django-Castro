from unittest import mock
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import Template, Context, loader
from articulos.models import article
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

# Create your views here.

class ArticuloList(ListView):
    model=article
    template_name= 'articulos.html'

class ArticuloDetalle(DetailView):
    model=article
    template_name= 'leerarticulo.html'

class creararticulo(CreateView):
    model=article
    success_url='/articulos/'
    fields = ['titulo', 'abstract', 'articulo', 'autor','image' ]

class modarticulo(UpdateView):
    model=article
    success_url='/articulos/'
    fields = ['titulo', 'abstract', 'articulo']

class deletearticulo(DeleteView):
    model=article
    success_url='/articulos/'

