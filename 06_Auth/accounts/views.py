from django.shortcuts import render
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login as auth_login

# Create your views here.
def login(request):
    if request.method == 'POST':
        form = AuthenticationForm()

    else:
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            # 아이디, 비밀번호가 일치한다면
            # 해당 유저 정보를 받아온다.
            user = form.get_user()
            auth_login(request, user)
            return redirect('articles:index')
    context = {'form':form}
    return render(request, 'accounts/login.html', context)