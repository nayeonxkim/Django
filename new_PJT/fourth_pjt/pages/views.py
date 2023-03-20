from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'pages/index.html', {'name':'김나연'})