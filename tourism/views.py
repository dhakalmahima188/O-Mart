from django.shortcuts import render
from .models import desitnation
# Create your views here.


def index(request):
    dst1 = desitnation()
    dst1.name = "Paris"
    dst1.desc = "The City of Light"
    dst1.price = "$200"
    dst1.img="desitnation_1.jpg"
    dst1.is_featured=True
    
    dst2 = desitnation()
    dst2.name = "Paris"
    dst2.desc = "The City of Light"
    dst2.price = "$200"
    dst2.img="desitnation_2.jpg"
    dst2.is_featured=False

    dst3 = desitnation()
    dst3.name = "Paris"
    dst3.desc = "The City of Light"
    dst3.price = "$200"
    dst3.img="desitnation_3.jpg"
    dst3.is_featured=False
    dst = [dst1, dst2, dst3]

    return render(request, 'index.html', {'dests': dst})
