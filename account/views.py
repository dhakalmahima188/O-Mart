from django.shortcuts import redirect, render,HttpResponse
from django.contrib.auth.models import User,auth
# Create your views here.
def register(request):
    # return HttpResponse("hello world")

    if request.method == 'POST':
        first_name = request.POST['fname']
        last_name = request.POST['lname']
        username = request.POST['uname']
        password = request.POST['password']
        email = request.POST['email']

        user=User.objects.create(username=username,password=password,first_name=first_name,last_name=last_name,email=email)
        user.save()
        print("USer created")
        return redirect('/')
    else:        
        return render(request, 'register.html')