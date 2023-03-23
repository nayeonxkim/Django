from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login as auth_login
# Create your views here.
def login(request):
    if request.method == 'POST':
        # 데이터베이스를 조작하는 요청인 POST가 오면
        # 로그인 처리(데이터베이스를 조작)한다.
        
        # 입력한 아이디, 비밀번호가 일치하는지 검사한다.
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            auth_login(request, form.get_user())
            return redirect('article:index')


    else:
        # 비어있는 로그인 페이지를 제공한다.
        form = AuthenticationForm()

    context ={'form':form}
    return render(request, 'accounts/login.html', context)
    
