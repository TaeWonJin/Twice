from django.shortcuts import render
from .models import Twice

def twice(request):
    members=Twice.objects.filter(nationality='JP')
    return render(request, 'home.html' ,{'japanese':members})
