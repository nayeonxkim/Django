from django.shortcuts import render, redirect
from .models import Article

# Create your views here.
def index(request):
    articles = Article.objects.all()
    context = {
        'articles' : articles
    }
    return render(request, 'articles/index.html', context)


def detail(request, article_pk):

    # Article클래스에서 id가 article_pk인 애를 찾아온다.
   article =  Article.objects.get(id=article_pk)
   context = {
       
        'article': article
    }

   return render(request, 'articles/detail.html', context)

def new(request):
    return render(request, 'articles/new.html')



def create(request):
    # 게시글 생성 요청 -> 응답 : 게시글 생성만 해주면 됨.
    # 게시글 생성한 뒤에, 특정 페이지를 사용자에게 반환한다.


    # 1. 게시글을 생성한다.
    article = Article()
    article.title = request.POST.get('title')
    article.content = request.POST.get('content')
    article.save()

    # 2. 다른 요청 경로로 이동시킨다.
    return redirect('articles:detail', article.pk)


def edit(request, article_pk):
    article = Article.objects.get(id=article_pk)
    context ={
        'article':article
    }
    return render(request, 'articles/edit.html', context)

def update(request, article_pk):
    
    article = Article.objects.get(id=article_pk)
    article.title = request.POST.get('title')
    article.content = request.POST.get('content')
    article.save()
    return redirect('articles:detail', article.pk)

def delete(request, article_pk):

    article = Article.objects.get(id=article_pk)
    article.delete()
    
    return redirect('articles:index')