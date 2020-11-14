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
            'title': 'HotTitle ' + str(i),
            'id': i,
            'text': 'HotText' + str(i),
            'rating': 999,
            'answers': i,
            'tags': ['hot topic', 'hot', 'melting'],
        })
    return render(request, 'hot.html', {
        'questions': hotQuestions_,
        'rightPanel': rightPanel,
    })


def tagQuestions(request, tag):
    taggedQuestions_ = []
    for i in range(1, 5):
        taggedQuestions_.append({
            'title': 'TaggedQuestion' + str(i),
            'id': i,
            'text': 'TaggedText' + str(i),
            'rating': 50 + i,
            'answers': i,
            'tags': ['a', 'b', tag],
        })
    return render(request, 'tag.html', {
        'tag': tag,
        'questions': taggedQuestions_,
        'rightPanel': rightPanel,
    })


def question(request, id):
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
