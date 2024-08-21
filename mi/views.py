from django.shortcuts import render
from django.http import HttpResponse

def caption(request):
    return HttpResponse('Rohit sharma is best hitter in world')


def vice(request):
    return HttpResponse('surya is best finisher in india ')

