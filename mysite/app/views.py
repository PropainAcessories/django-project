from django.http import HttpResponse
from .models import Post

def index(request):
  recent_post_list = Post.objects.order_by('-post_date')[:5]
  output = ','.join([p.post_text for p in recent_post_list])
  return HttpResponse(output)

def detail(request, post_id):
    return HttpResponse("You're looking at post %s." % post_id)

def results(request, post_id):
    response = "You're looking at the results of post %s."
    return HttpResponse(response % post_id)

def vote(request, post_id):
    return HttpResponse("You're voting on post %s." % post_id)