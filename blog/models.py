from django.db import models
from django.utils import timezone


class Post(models.Model):
    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

class User(models.Model):
    name=models.CharField(max_length=50)

class Point(models.Model):
    artist=models.CharField(max_length=50)
    point=models.DecimalField(max_digits=2,decimal_places=0)
    user=models.ForeignKey(User)