from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'index.html',{'price':'800','name':'Lumbini','desc':'Lumbini is a holy place.'})