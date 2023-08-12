from django.urls import path

from service import views

urlpatterns = [
    path('', views.index, name='index'),
    path('kca-list', views.kca_list, name='kca_list'),
]
