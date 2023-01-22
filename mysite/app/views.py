from django.http import HttpResponse
from django.http import Http404
from .models import Post
from django.shortcuts import render

def index(request):
  recent_post_list = Post.objects.order_by('-post_date')[:5]
  context = {
      'recent_post_list': recent_post_list,
    }
  return render(request, 'posts/index.html', context)


def detail(request, post_id):
  try:
    post = Post.objects.get(pk=post_id)
  except Post.DoesNotExist:
    raise Http404("Post Does Not Exist.")
  
  return  render(request, 'posts/detail.html', {'post': post})

def results(request, post_id):
  response = "You're looking at the results of post %s."
  return HttpResponse(response % post_id)

def vote(request, post_id):
  return HttpResponse("You're voting on post %s." % post_id)