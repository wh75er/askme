from django.http import HttpRequest
from django.shortcuts import render

from app.models import paginate, get_popular_tags, Question, Answer

rightPanel = {
    'popularTags': [
            'tag1',
            'tag2',
            'tag3',
            'tag4',
            'tag5'
        ],
    'bestMembers': [
        {
            'name': 'member1'
        },
        {
            'name': 'member2'
        },
        {
            'name': 'member3'
        },
    ]
}




def index(request):
    questions_ = Question.objects.get_newest()

    page, pages, questions_ = paginate(questions_, request, 20)

    return render(request, 'index.html', {
        'page': page,
        'pages': pages,
        'questions': questions_,
        'rightPanel': rightPanel,
    })


def hotQuestions(request):
    questions_ = Question.objects.get_hottest()

    page, pages, questions_ = paginate(questions_, request, 20)

    return render(request, 'hot.html', {
        'page': page,
        'pages': pages,
        'questions': questions_,
        'rightPanel': rightPanel,
    })


def tagQuestions(request, tag):
    questions_ = Question.objects.get_bytag(tag)

    page, pages, questions_ = paginate(questions_, request, 20)

    return render(request, 'tag.html', {
        'page': page,
        'pages': pages,
        'tag': tag,
        'questions': questions_,
        'rightPanel': rightPanel,
    })


def question(request, id):
    question_ = Question.objects.get(pk=id)
    answers_ = Answer.objects.filter(question=question_)

    page, pages, answers_ = paginate(answers_, request, 30)

    return render(request, 'question.html', {
        'page': page,
        'pages': pages,
        'entity': question_,
        'answers': answers_,
        'single_page': True,
        'rightPanel': rightPanel,
    })


def login(request):
    return render(request, 'login.html', {
        'rightPanel': rightPanel,
    })


def signup(request):
    return render(request, 'signup.html', {
        'rightPanel': rightPanel,
    })


def ask(request):
    return render(request, 'ask.html', {
        'rightPanel': rightPanel,
    })


def settings(request):
    return render(request, 'settings.html', {
        'rightPanel': rightPanel,
    })
