from django.shortcuts import render
from .models import desitnation
# Create your views here.


def index(request):
    dst=desitnation.objects.all()

    return render(request, 'index.html', {'dests': dst})
