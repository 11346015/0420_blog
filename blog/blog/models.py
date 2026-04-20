from django.db import models
from django.urls import reverse

class Author(models.Model):
    name = models.CharField(max_length=100, verbose_name="作者姓名")

    def __str__(self):
        return self.name

class Post(models.Model):
    title = models.CharField(max_length=200)
    # 將原本的 "auth.User" 改為連結到上面的 Author 類別
    author = models.ForeignKey(
        Author, 
        on_delete=models.CASCADE,
        related_name="posts"
    )
    body = models.TextField()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("post_detail", kwargs={"pk": self.pk})