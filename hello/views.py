from django.shortcuts import render
from .models import Post

posts = [
      {
        'author': 'JohnFuhrm',
        'title': 'Blog Post 1',
        'content': 'First Post Content',
        'date_posted': 'August 27, 2021'
      },
      {
        'author': 'Jane Doe',
        'title': 'Blog Post 2',
        'content': 'Second Post Content',
        'date_posted': 'August 28, 2021'
      }
]

def index(request):
  return render(request, 'index.html')

def page(request):
  return render(request, 'page.html')

def test(request):
  context = {
    'posts': posts
  }
  return render(request, 'testpage.html', context)