from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    questions_ = []
    for i in range(1, 30):
        questions_.append({
            'title': 'title ' + str(i),
            'id': i,
            'text': 'text' + str(i),
            'rating': 2,
            'answers': i,
            'tags': ['simple', 'small'],
        })
    questions_[0]['rating'] = 200
    return render(request, 'index.html', {
        'questions': questions_,
    })


def hotQuestions(request):
    hotQuestions_ = []
    for i in range(1, 10):
        hotQuestions_.append({
            'title': 'title ' + str(i),
            'id': i,
            'text': 'text' + str(i),
            'rating': 200,
            'tags': ['a', 'b'],
        })
    return HttpResponse("hot questions page")


def tagQuestions(request, tag):
    taggedQuestions_ = []
    for i in range(1, 5):
        taggedQuestions_.append({
            'title': 'title ' + str(i),
            'id': i,
            'text': 'text' + str(i),
            'rating': 200,
            'tags': ['a', 'b', tag],
        })
    return HttpResponse("tagged questions page: %s" % tag)


def question(request, id):
    print("id is :", id)
    question_ = {
            'title': 'Hello world',
            'id': id,
            'text': 'yo, whats up',
            'rating': 200,
            'tags': ['a', 'b'],
            }
    print("dict is: ", question_)
    answers_ = []
    for i in range(1, 30):
        answers_.append({
            'title': 'title ' + str(i),
            'id': i,
            'text': 'text' + str(i),
            'rating': 222,
            'correct': False,
        })
    return HttpResponse("question page: %s" % question_['id'])


def login(request):
    return HttpResponse("login page")


def signup(request):
    return HttpResponse("sign-up page")


def ask(request):
    return HttpResponse("question creation page")
