from django.shortcuts import render
from django.http import HttpResponse

def caption(request):
    return HttpResponse('MSD is BEST WK')


def vice(request):
    return HttpResponse('Suresh Raina is MR IPL PERFECT')


