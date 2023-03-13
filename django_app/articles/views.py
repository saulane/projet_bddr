from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.template import loader
from .models import Article,Subtheme,Theme, Author, Laboratory
from django.db.models.functions import TruncMonth,TruncYear, TruncWeek
from django.db.models import Count


def articles(request):
    title = request.GET.get('title')
    subtheme = request.GET.getlist('subtheme[]')
    date = request.GET.get('date')
    labo = request.GET.get('labo')

    q = Article.objects
    if len(title) > 0:
        q = q.filter(title__unaccent__icontains=title)

    if subtheme:
        q = q.filter(subtheme_id__in=subtheme)

    if date:
        date = date.split("-")
        q = q.filter(date__year=date[0])
    context = {"res": q,"title":title}


    template = loader.get_template('articles.html')
    return HttpResponse(template.render(context))

def article(request, doi):
    template = loader.get_template('article.html')
    obj = Article.objects.get(doi=doi)
    
    return HttpResponse(template.render())

def home(request):
    context = {"subthemes": Subtheme.objects.all(),
               "labos": Laboratory.objects.all(),
               "themes": Theme.objects.all()}

    template = loader.get_template('index.html')
    return HttpResponse(template.render(context))


def articles_count_by_month(request):
    data = Article.objects.annotate(month=TruncMonth('date')).values('month').annotate(count_items=Count('id')).values('month','count_items').order_by('month')[::-1][:30][::-1]
    return JsonResponse(list(data), safe=False)

def articles_count_by_year(request):
    data = Article.objects.annotate(year=TruncYear('date')).values('year').annotate(count_items=Count('id')).values('year','count_items').order_by('year')[::-1][:20][::-1]
    return JsonResponse(list(data), safe=False)

def articles_count_by_week(request):
    data = Article.objects.annotate(week=TruncWeek('date')).values('week').annotate(count_items=Count('id')).values('week','count_items').order_by('week')[::-1][:50][::-1]
    return JsonResponse(list(data), safe=False)