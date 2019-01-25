from django.conf.urls import url, include
from django.urls import path

from . import views

urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    # path('articles/', views.articles, name='articles'),
    # path('articles/<int:pk>/', views.article_details, name='article_details')
]