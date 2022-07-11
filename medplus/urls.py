from django.urls import path
from medplus import views

app_name = 'medplus'

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('about/', views.about, name='about'),
    path('search/', views.search, name='search'),
    path('data/', views.data, name='data'),
    path('map/', views.map, name='map'),
    path('subscribe/', views.subscribe, name='subscribe'),
]
