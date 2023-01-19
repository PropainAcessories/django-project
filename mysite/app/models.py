from django.db import models

# Create your models here.
class Post(models.Model):
  post_text = models.CharField(max_length=3000)
  post_date = models.DateField('date published')
  votes = models.IntegerField(default=0)

class Comment (models.Model):
  post = models.ForeignKey(Post,
  on_delete=models.CASCADE)
  answer_text = models.CharField(max_length=3000)
  votes = models.IntegerField(default=0)