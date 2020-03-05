from django.db import models
import datetime as dt
from django.contrib.auth.models import User
from tinymce.models import HTMLField

class Tags(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class Article(models.Model):
    title = models.CharField(max_length=60)
    post = HTMLField()
    # one-many-relationship
    editor = models.ForeignKey(User, on_delete=models.CASCADE)
    # many-many-relationship
    tags = models.ManyToManyField(Tags)
    pub_date = models.DateTimeField(auto_now_add=True)
    article_image = models.ImageField(upload_to='articles/', default="default-no-image-1.png")

    @classmethod
    def todays_news(cls):
        today = dt.date.today()
        news = cls.objects.filter(pub_date__date=today)
        return news

    @classmethod
    def days_news(cls, date):
        news = cls.objects.filter(pub_date__date=date)
        return news

    @classmethod
    def search_by_title(cls, search_term):
        news = cls.objects.filter(title__icontains=search_term)
        return news


class NewsLetterRecipients(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField()