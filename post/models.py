from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Posts(models.Model):
    # user=models.ForeignKey(User)
    # email=models.EmailField(max_length=100,unique=True,null=False,blank=False)
    author = models.ForeignKey(User , on_delete = models.CASCADE)
    title = models.CharField(max_length = 100)
    url = models.CharField(max_length = 2083,null = True,blank = True)
    description = models.TextField()
    datetime_added = models.DateTimeField(auto_now_add = True)
    datetime_modified = models.DateTimeField(auto_now = True)


class Blog(models.Model):
    author = models.ForeignKey(User , on_delete = models.CASCADE)
    blogtitle = models.CharField(max_length = 200)
    content = models.TextField()
    datetime_added = models.DateTimeField(auto_now_add = True)
    datetime_modified = models.DateTimeField(auto_now = True)
