from django.urls import path
from . import views



app_name = 'articles'

urlpatterns = [
    path('index/', views.index, name = 'index'),
    # name? 이 path자체를 부를 이름
    path('create/', views.create, name = 'create'),
    path('<str:name>/profile/', views.profile, name='profile'),
    path('<int:age>/', views.info, name='info')
]

