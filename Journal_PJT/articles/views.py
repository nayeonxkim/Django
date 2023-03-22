from django.shortcuts import render, redirect
from .forms import ArticleForm
from .models import Article

# Create your views here.
def index(request):
    articles = Article.objects.all()
    context ={'articles':articles}
    return render(request, 'articles/index.html', context)



def create(request):
    if request.method == 'GET':
        form = ArticleForm()
        
    else:
        form = ArticleForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('articles:index')

    context = {'form':form}
    return render(request, 'articles/create.html', context)



def detail(request, article_pk):
    article = Article.objects.get(pk=article_pk)
    context = {'article':article}
    return render(request, 'articles/detail.html', context)
    

    