from django.db import models
from django.contrib.auth.models import AbstractUser


class Category(models.Model):
    title = models.CharField(max_length=200)

    class Meta:
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.title


class News(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    title = models.CharField(max_length=300)
    image = models.ImageField(upload_to='imgs/upload/')
    body = models.TextField()
    time = models.DateTimeField(auto_now_add=True)
    view = models.IntegerField(default='0')
    cmtCount = models.IntegerField(default='0')

    class Meta:
        verbose_name_plural = 'News'

    def __str__(self):
        return self.title


class Comment(models.Model):
    news = models.ForeignKey(News, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    body = models.TextField()
    time = models.DateTimeField(auto_now_add=True)
    status = models.BooleanField(default=False)

    class Meta:
        verbose_name_plural = 'Comments'

    def __str__(self):
        return self.body


class Member(AbstractUser):
    interest = models.ManyToManyField(Category, blank=True, verbose_name='interest')
