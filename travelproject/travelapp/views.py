from django.contrib import messages
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import place, Guides


# Create your views here.
def demo(request):
    obj = place.objects.all()
    obj2 = Guides.objects.all()
    return render(request, 'index.html', {'result': obj,'result2': obj2})
