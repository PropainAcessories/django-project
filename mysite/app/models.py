import datetime
from django.db import models
from django.utils import timezone

# Create your models here.
class Post(models.Model):
  post_text = models.CharField(max_length=3000)
  post_date = models.DateField('date published')
  votes = models.IntegerField(default=0)

  def __str__(self):
    return self.post_text
  
  def was_published_recently(self):
    return self.post_date >= timezone.now() - datetime.timedelta(days=1)

class Comment (models.Model):
  post = models.ForeignKey(Post,
  on_delete=models.CASCADE)
  answer_text = models.CharField(max_length=3000)
  votes = models.IntegerField(default=0)

  def __str__(self):
    return self.answer_text