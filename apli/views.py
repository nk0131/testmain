from django.shortcuts import render
from django.views import generic
from django.views.generic import TemplateView

class IndexView(generic.TemplateView):
    template_name = 'index.html'