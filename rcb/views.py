from django.shortcuts import render
from django.http import HttpResponse

def caption(request):
    return HttpResponse('virat is best batsman in world')


def vice(request):
    return HttpResponse('abd is 360 ')



