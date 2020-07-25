from django.urls import path

from . import views

app_name = 'myapp'
urlpatterns = [
    path('', views.home_view, name="home"),
    path('about/', views.about_view),
    path('about-me/', views.about_view, name="about"),
    path('start/', views.home_view),
    path('contact/', views.contact_view, name="contact"),
]
