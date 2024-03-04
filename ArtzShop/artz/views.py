from django.shortcuts import render
from django.http import HttpResponse
from .models import Artz


def home(request):
    Artz_ = Artz.objects.all()
    return render(request, 'home.html', {'Artz': Artz_})
