from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Article

def articles(request):
    s = request.GET.get('title')
    print(s)
    context = {"res": Article.objects.filter(title__icontains=s)}

    template = loader.get_template('articles.html')
    return HttpResponse(template.render(context))

def home(request):
    template = loader.get_template('index.html')
    return HttpResponse(template.render())