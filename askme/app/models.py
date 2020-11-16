import os
import math

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


# Create your models here.


class Rating(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)


class QuestionRating(models.Model):
    id = models.OneToOneField('Rating', on_delete=models.CASCADE, db_index=False, primary_key=True)
    questionId = models.ForeignKey('Question', on_delete=models.CASCADE)


class AnswerRating(models.Model):
    id = models.OneToOneField(Rating, on_delete=models.CASCADE, db_index=False, primary_key=True)
    answerId = models.ForeignKey('Question', on_delete=models.CASCADE)


class Question(models.Model):
    title = models.CharField(max_length=1024)
    text = models.TextField()
    raitingValue = models.IntegerField(default=0)
    avatar = models.FilePathField(path=images_path(), default = 'qimg.jpg')


class Answer(models.Model):
    question = models.ForeignKey('Question', on_delete=models.CASCADE)
    text = models.TextField()
    raitingValue = models.IntegerField(default=0)


class Tag(models.Model):
    question = models.ForeignKey('Question', on_delete=models.CASCADE)
    text = models.CharField(max_length=60)


class Profile(models.Model):
    id = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    avatar = models.FilePathField(path=images_path(), default = 'qimg.jpg')

