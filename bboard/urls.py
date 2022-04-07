from django.contrib import admin
from django.urls import path
from .views import index, by_rubric, BbCreateView


urlpatterns = [
    path('<int:rubric_id>/', by_rubric, name='by_rubric'),
    path('/index/main/', index, name='index'),
    path('add/', BbCreateView.as_view() , name='add'),

]
