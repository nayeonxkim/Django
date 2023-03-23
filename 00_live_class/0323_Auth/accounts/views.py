from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout

# Create your views here.
def login(request):
    # 로그인하는 것은 데이터베이스를 조작하는 요청이므로 method가 POST다.
    if request.method == 'POST':
        # 폼을 받아서 유효성 검사를 하는 것 -> 다 있음
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            auth_login(request, form.get_user())
            # get_user: 폼 내용과 일피하는 유저 가져옴
            return redirect('articles:index')
    else:
        # GET요청은 비어있는 로그인 화면을 보여달라는 것.
        form = AuthenticationForm()

    context ={'form':form}
    return render(request, 'accounts/login.html', context)



def logout(request):
    auth_logout(request)
    return redirect('articles:index')
