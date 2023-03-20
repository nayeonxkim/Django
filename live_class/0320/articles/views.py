from django.shortcuts import render, redirect
from .models import Article

# Create your views here.
def index(request):
    articles = Article.objects.all()
    context = {
        'articles' : articles 
    }
    return render(request, 'articles/index.html', context)


def detail(request, pk):
    articles = Article.objects.get(pk=pk)
    context = {
        'articles' : articles 
    }
    return render(request, 'articles/detail.html', context)

def new(request):
    return render(request, 'articles/new.html')


def create(request):
    # 데이터를 가져온다.
    title = request.POST.get('title')
    content = request.POST.get('content')

    # 가져온 데이터를 DB에 저장한다.
    article = Article(
        title = title,
        content = content
    )
    article.save()
    
    # Article.objects.create(
    #     title = title,
    #     content = content
    # )

    # 저장된 데이터를 index페이지에서 보여준다.
    return redirect('articles:index')