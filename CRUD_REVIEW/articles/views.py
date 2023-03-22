from django.shortcuts import render, redirect
from .models import Article

# forms.py에서 저장한 모델폼을 받아와서 context로 끌어와야
# 해당 데이터를 html파일에서 사용할 수 있다.
# 어떤 것이든 create는 아무 데이터도 받아올 수 없다.
# 무조건 views에서 context로 받아서 넘겨주는 것이다.
from .forms import ArticleForm
# Create your views here.



def index(request):
    articles = Article.objects.all()
    context = {
        'articles' : articles
    }
    return render(request, 'articles/index.html', context)


# GET 메서드 요청 -> 게시글 생성 페이지 조회
# POST 메서드 요청 -> 게시글 생성을 위해 DB에 저장
def create(request):

    # 제출 버튼 클릭 = POST 요청
    if request.method == 'POST':

        # 작성한 내용이 담겨있는 폼을 form변수에 담는다.
        form = ArticleForm(request.POST)
        
        # form이 유효하다면, DB에 저장한다.
        if form.is_valid():
            form.save()
            ### 여기까지하면 POST요청에 대한 응답은 끝.
            ## 그런데 아무것도 return안해주면 오류난다. -> 무조건 뭐 한페이지는 보여줘야함.
            return redirect('articles:index')


    else:

        # ArticleForm을 받아와서 form인스턴스를 생성한다.
        # GET요청이 오면 폼을 만들어주기만 한다.
        form = ArticleForm()

    context = {'form' : form} 
    return render(request, 'articles/create.html', context)




def detail(request, article_pk):

    # 받아온 article_pk와 pk가 일치하는 게시글을 get해서 article변수에 저장한다.
    article = Article.objects.get(pk = article_pk)
    context ={
        'article' : article
    }
    return render(request, 'articles/detail.html', context)


def update(request, article_pk):
     # article_pk와 pk가 일치하는 게시글을 가져온다.
    article = Article.objects.get(pk=article_pk)

    ### POST 요청 응답
    if request.method == 'POST':
        # 1
        form = ArticleForm(request.POST, instance=article)
        if form.is_valid():
            form.save()
            return redirect('articles:detail', article.pk)



    ### GET요청 응답
    else:
        form = ArticleForm(instance=article)

    # POST 요청이 들어왔을 떄, 유효성 검사를 통과하지 못한다면 아래 코드가 실행되어야한다. 따라서 else문 밖에 있어야한다.
    context = {'form':form} 
    return render(request, 'articles/update.html', context)
