import os
import math

from datetime import datetime

from django.contrib.auth.models import User
from django.db import models

from django.conf import settings


def images_path():
    return os.path.join(settings.BASE_DIR, 'static/img/')


def paginate(objectsList, request, perPage=10):
    size = len(objectsList)
    pages = math.ceil(size/perPage)

    page = request.GET.get('page', '')

    if page == '':
        page = 1

    page = int(page)

    startIdx = (page - 1) * perPage
    pageSlice = objectsList[startIdx:startIdx + perPage]

    return page, pages, pageSlice


def get_popular_tags():
    tags = Tag.objects.annotate(tag_count=models.Count('text')) \
        .order_by('-tag_count') \
        .reverse()[:20]

    tags_list = []
    for tag in tags:
        tags_list.append(tag.text)

    return tags_list


def get_best_members():
    one_week_ago = datetime.today() - datetime.timedelta(days=7)
    questions = Question.objects.filter(date_gte=one_week_ago) \
        .order_by('rating') \
        .reverse()[:10]

    members = []
    for question in questions:
        members.append(question.get(user__username))

    return members


# Create your models here.

class QuestionRating(models.Model):
    DISLIKE = 'DK'
    LIKE = 'LK'
    LIKE_TYPE_CHOICES = [
                 (DISLIKE, 'DISLIKE'),
                 (LIKE, 'LIKE')
                ]
    like_type = models.CharField(
        max_length=2,
        choices=LIKE_TYPE_CHOICES,
        default=LIKE,
    )
    question = models.ForeignKey('Question',
                                 null=True,
                                 on_delete=models.CASCADE)
    user = models.ForeignKey(User,
                             on_delete=models.CASCADE)

    class Meta:
        unique_together = ['question', 'user']


class AnswerRating(models.Model):
    DISLIKE = 'DK'
    LIKE = 'LK'
    LIKE_TYPE_CHOICES = [
                 (DISLIKE, 'DISLIKE'),
                 (LIKE, 'LIKE')
                ]
    like_type = models.CharField(
        max_length=2,
        choices=LIKE_TYPE_CHOICES,
        default=LIKE,
    )
    answer = models.ForeignKey('Answer',
                               null=True,
                               on_delete=models.CASCADE)
    user = models.ForeignKey(User,
                             on_delete=models.CASCADE)

    class Meta:
        unique_together = ['question', 'user']


class QuestionManager(models.Manager):
    def get_newest(self):
        questions = self.order_by('date')

        return questions

    def get_hottest(self):
        questions = self.order_by('rating').reverse()

        return questions

    def get_bytag(self, tag_):
        questions = self.filter(tag__text=tag_)

        return questions

    def get_tags(self):
        return self.get(tag).all()


class Tag(models.Model):
    text = models.CharField(max_length=60)

    def __str__(self):
        return str({'text': self.text})


class Question(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=1024)
    text = models.TextField()
    answers = models.IntegerField(default=0)
    rating = models.IntegerField(default=0)
    avatar = models.FilePathField(path=images_path(), default='qimg.jpg')
    date = models.DateTimeField(auto_now_add=True)
    tag = models.ManyToManyField(to=Tag)

    objects = QuestionManager()

    def __str__(self):
        return str({'title': self.title,
                    'text': self.text,
                    'answers': self.answers,
                    'rating': self.rating,
                    'avatar': self.avatar,
                    'date': self.date})


class Answer(models.Model):
    question = models.ForeignKey('Question', on_delete=models.CASCADE)
    text = models.TextField()
    rating = models.IntegerField(default=0)
    correct = models.BooleanField(default=False)


class Profile(models.Model):
    id = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    avatar = models.FilePathField(path=images_path(), default='qimg.jpg')
