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
    answerId = models.ForeignKey('Answer', on_delete=models.CASCADE)


class QuestionManager(models.Manager):
    def get_newest(self):
        questions = self.order_by('date')

        tags_qset = []
        for question_ in questions:
            tag = Tag.objects.filter(question=question_)
            tags_qset.append(tag.values('text'))

        questions = questions.values()

        for i in range(len(questions)):
            questions[i]['tags'] = []
            for tags in tags_qset[i]:
                print(tags)
                questions[i]['tags'].append(tags['text'])

        return questions

    def get_hottest(self):
        return self.order_by(rating)

    def get_byid(self, id_):
        return self.filter(self=id_)

    def get_bytag(self, tag_):
        return self.filter(self=Tag.filter(Tag__text=tag_).only(question))
    
    def get_tags(self):
        return Tag.filter(Tag__id=self)


class Question(models.Model):
    title = models.CharField(max_length=1024)
    text = models.TextField()
    answers = models.IntegerField(default=0)
    rating = models.IntegerField(default=0)
    avatar = models.FilePathField(path=images_path(), default = 'qimg.jpg')
    date = models.DateTimeField(auto_now_add=True)

    objects = QuestionManager()
    
    def __str__(self):
        return str({'title': self.title, 'text': self.text, 'answers': self.answers, 'rating': self.rating, 'avatar': self.avatar, 'date': self.date})


class Answer(models.Model):
    question = models.ForeignKey('Question', on_delete=models.CASCADE)
    text = models.TextField()
    rating = models.IntegerField(default=0)
    correct = models.BooleanField(default=False)


class Tag(models.Model):
    question = models.ForeignKey('Question', on_delete=models.CASCADE)
    text = models.CharField(max_length=60)

    def __str__(self):
        return str({'question id': self.question, 'text': self.text})


class Profile(models.Model):
    id = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    avatar = models.FilePathField(path=images_path(), default = 'qimg.jpg')
    
