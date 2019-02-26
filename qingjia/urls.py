from django.conf.urls import url
from django.urls import path

from . import views

urlpatterns = [
    path('', views.index),
    path('post_index/post_info/', views.post_info),
    path('post_index/', views.post),
    path('post_index/error/', views.index),
]