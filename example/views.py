from django.http import HttpResponse
from django.shortcuts import render
from .task import *


def index(request):
    # sleepy(10)
    return HttpResponse(parseFromMechta().delay(), content_type="application/json")
