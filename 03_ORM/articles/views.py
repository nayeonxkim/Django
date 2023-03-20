from django.shortcuts import render
from models import Article

# Create your views here.
def index(request):
    return render(request, 'articles/index.html')

def new(request):
    return render(request, 'articles/new.html')


def create(request):
    title = request.GET.get('title')
    content = request.GET.get('content')

    Article
    return render(request, 'articles/create.html')