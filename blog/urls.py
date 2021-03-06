from django.urls import path

from blog.views import *

urlpatterns = [
    path('', index, name='home'),
    path('posts/', posts_list, name='posts_list'),
    path('post/<str:slug>/', PostDetail.as_view(), name='post_detail'),
    path('tags/', tags_list, name='tags_list'),
    path('tag/<str:slug>/', TagDetail.as_view(), name='tag_detail'),
]