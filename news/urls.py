from django.urls import path

from . import views

app_name = 'news'
urlpatterns = [
    path('', views.index, name='home'),
    path('<source>/', views.index, name='index'),
]
