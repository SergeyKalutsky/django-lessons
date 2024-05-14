from datetime import datetime
from random import randint
from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    context = {'number': randint(1, 100)}
    return render(request, 'random.html', context)


def score(request):
    context = {'score': randint(1, 100)}
    return render(request, 'score.html', context)


def daytime(request):
    hour = datetime.now().hour
    context = {'hour': hour, 'user': 'Сергей'}
    return render(request, 'daytime.html', context)


def score_and_time(request):
    hour = datetime.now().hour
    context = {'hour': hour, 'user': 'Сергей', 'score': randint(1, 100)}
    return render(request, 'score_and_time.html', context)


def lootbox(request):
    loot = randint(1, 100)
    context = {'loot': loot}
    return render(request, 'lootbox.html', context)