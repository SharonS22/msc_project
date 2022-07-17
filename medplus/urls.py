from django.urls import path
from medplus import views

app_name = 'medplus'

urlpatterns = [
    path('index/', views.index, name='index'),
] 
