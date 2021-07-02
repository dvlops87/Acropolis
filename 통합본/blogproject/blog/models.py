from functools import update_wrapper
from django.db import models


# Create your models here.

class Blog(models.Model) :
    Qnum = models.CharField(max_length=20,null = True,default='')
    title = models.CharField(max_length=200,default='')
    num1 = models.CharField(max_length=100,default='')
    num2 = models.CharField(max_length=100,default='')
    num3 = models.CharField(max_length=100,default='')
    num4 = models.CharField(max_length=100,default='')
    answer = models.CharField(max_length=10,default='')
    othercomment = models.TextField(null = True)
    explain = models.TextField(null = True)

    def __str__(self):
        return self.title


class Comment(models.Model):
    content = models.CharField(max_length=200)
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
    bodys= models.CharField(max_length=200,default='')
    writer= models.CharField(max_length=200,default='')

    def __str__(self):
        return self.content

