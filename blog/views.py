from django.shortcuts import render
from .models import Post
posts =  [
    {
        'author': 'Jesse Shea',
        'title': 'WTF',
        'content': 'Is i Learning?',
        'date_posted': 'yesterday'
    },
    {
        'author': 'Jimmy Pop',
        'title': 'Tickle sandwich',
        'content': 'DEEERRPPPP',
        'date_posted': 'next year'
    }
]

def home(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'blog/home.html', context)

def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})

