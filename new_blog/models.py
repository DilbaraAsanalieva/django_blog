from django.db import models


class Blog(models.Model):
    image = models.FileField(upload_to="blog_images/")
    title = models.CharField(max_length=120)
    description = models.TextField()
    likes = models.IntegerField(default=0)
    reposts = models.IntegerField(default=0)

class Comment(models.Model):
    date = models.DateTimeField(auto_now_add=True)
    text = models.CharField(max_length=100)
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)

