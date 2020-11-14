from django.http import HttpResponse
from django.shortcuts import render

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
        'rightPanel': rightPanel,
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
            'title': 'Question ' + str(id),
            'id': id,
            'text': 'yo, whats up. I have a stupid question',
            'rating': 200,
            'tags': ['stupid question', 'question'],
            }
    answers_ = []
    for i in range(1, 30):
        answers_.append({
            'id': i,
            'text': 'AnswerText' + str(i),
            'rating': i+1,
            'correct': False,
        })
    return render(request, 'question.html', {
        'entity': question_,
        'answers': answers_,
    })


def login(request):
    return HttpResponse("login page")


def signup(request):
    return HttpResponse("sign-up page")


def ask(request):
    return HttpResponse("question creation page")
