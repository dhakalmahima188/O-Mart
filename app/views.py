from django.http import HttpResponse
from django.shortcuts import render
def home(request):
    return render(request,'home.html',{'title':'Home'})
    
def add(request):
    val1=int(request.POST['a'])
    val2=int(request.POST['b'])
    res=val1+val2
    print(res)
    return render(request,'add.html',{'result':res})
