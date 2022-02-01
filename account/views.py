from django.shortcuts import redirect, render,HttpResponse,redirect
from django.contrib.auth.models import User,auth

# Create your views here.
def register(request):
    # return HttpResponse("hello world")

    if request.method == 'POST':
        print("Post wala")
        first_name = request.POST['first_name']  
        username = request.POST['username']
        password = request.POST['password']
        email = request.POST['email']
        if User.objects.filter(username=username).exists():
            print("Username exists")
            return redirect('/account/register')
        else:
            user=User.objects.create_user(username=username,password=password,first_name=first_name,email=email)
            user.save();
            print("USer created")
            return redirect('/')
    else: 
        print("gayena hai")       
        return render(request, 'register.html')