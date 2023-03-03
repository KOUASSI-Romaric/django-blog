from django.shortcuts import render
from .models import Article


# Create your views here.
def home(request):
    list_article = Article.objects.all()
    context = {'list_article': list_article}
    return render(request, "article/index.html", context)


def detail(request, id_article):
    article = Article.objects.get(id=id_article)
    context = {'article': article}
    return render(request, 'article/detail.html', context)
