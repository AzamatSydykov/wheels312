from django.shortcuts import render

# Create your views here.
from django.views.generic import View
from .utils import *
from blog.models import Post, Tag


def index(request):
    return render(request, 'index.html')


def posts_list(request):
    posts = Post.objects.all()
    return render(request, 'posts_list.html', {'posts': posts})


def tags_list(request):
    tags = Tag.objects.all()
    return render(request, 'tags_list.html', {'tags': tags})


class PostDetail(ObjectDetailMixin, View):
    model = Post
    template = 'post_detail.html'


class TagDetail(ObjectDetailMixin, View):
    model = Tag
    template = 'tag_detail.html'