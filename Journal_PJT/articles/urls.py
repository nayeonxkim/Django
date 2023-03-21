from django.urls import path
from . import views

app_names = 'articles'

urlpatterns = [
    path('index/', views.index, name='index')
]

