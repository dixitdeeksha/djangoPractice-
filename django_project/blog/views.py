from multiprocessing import context
from django.shortcuts import render
from .models import Post

posts = [
    {
        'author': 'Deeksha Dixit',
        'title': 'Post 1',
        'content': '1st post by Deeksha Dixit',
        'date_posted': 'August,27,2018'
    },
    {
        'author': 'Name 2',
        'title': 'Post 2',
        'content': '2nd post by content',
        'date_posted': 'Date 2'
    },
]


def home(request):
    context = {'posts': Post.objects.all()
    }  # 2nd posts is posts dictronory
    return render(request, 'blog/home.html', context)


def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})
