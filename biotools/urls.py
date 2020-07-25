from django.urls import path

from . import views

app_name = 'biotools'
urlpatterns = [
    path('seqcontent', views.seqcontent_view, name='seqcontent'),
    path('revcomp', views.revcomp_view, name='revcomp'),
    path('randomdna', views.randomdna_view, name='randomdna')
]
