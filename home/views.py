from django.shortcuts import render
from django.views.generic import ListView, TemplateView, DetailView

# Create your views here.

class IndexView(TemplateView):
    template_name = 'home/index.html'


class AboutView(TemplateView):
    template_name = 'home/about.html'


