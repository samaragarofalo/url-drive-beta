import traceback

from django.http import HttpResponse
from django.shortcuts import render


def login(request):
    return render(request,'core/login.html')


def logout(request):
    return render(request, 'core/login.html')


def sign_up(request):
    return render(request, 'core/signup.html')
