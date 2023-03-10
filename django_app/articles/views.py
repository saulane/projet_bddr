from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Article,Subtheme,Theme, Author, Article_author

def articles(request):
    title = request.GET.get('title')
    subtheme = request.GET.get('subtheme')
    q = Article.objects
    if title:
        q = q.filter(title__icontains=title)

    if subtheme:
        q = q.filter(subtheme_id=subtheme)
    context = {"res": q}

    template = loader.get_template('articles.html')
    return HttpResponse(template.render(context))

def article(request, doi):
    template = loader.get_template('article.html')
    obj = Article.objects.get(doi=doi)
    authors_article = Article_author.objects.filter(article_id=obj).values_list("author_id", flat=True)
    authors = Author.objects.filter(pk__in=authors_article)
    context = {"res": obj,"authors":authors}
    
    return HttpResponse(template.render(context))

def home(request):
    context = {"subthemes": Subtheme.objects.all()}

    template = loader.get_template('index.html')
    return HttpResponse(template.render(context))