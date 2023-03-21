from django.urls import path
from . import views


app_name = 'articles'
urlpatterns = [
    path('index/', views.index, name='index'),
    path('create/', views.create, name='create'),

    # articles/정수/ -> 이 정수를 article_pk변수에 저장한다.
    path('<int:article_pk>/', views.detail, name='detail'),
    path('<int:article_pk>/update/', views.update, name='update'),

]