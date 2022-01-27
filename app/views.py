from django.http import HttpResponse
from django.shortcuts import render
def home(request):
    return render(request,'home.html',{'title':'Home'})
    
def add(request):
    val1=int(request.GET['a'])
    val2=int(request.GET['b'])
    res=val1+val2
    print(res)
    return render(request,'add.html',{'result':res})
