from django.contrib import auth
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login


# Create your views here.
def home(request):
    return render(request,"index.html")


def store(request):
    return render(request,"store.html")



def login_view(request):
        if request.method == 'POST':
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('store.html')
            else:
                messages.error(request, 'Invalid username or password')
        return render(request,'login.html')

def register_view(request):
        if request.method == 'POST':
            username = request.POST['username']
            first_name = request.POST['first_name']
            last_name = request.POST['last_name']
            email = request.POST['email']
            password = request.POST['password']
            cpassword = request.POST['cpassword']
            if User.objects.filter(username=username).exists():
                messages.error(request, 'Username already exists')
            elif password != cpassword:
                messages.error(request, 'Password and confirm password do not match')
            else:
                User.objects.create_user(username=username,first_name=first_name,last_name=last_name,email=email, password=password)
                messages.success(request, 'Registration successful. You can now log in.')
                return redirect('login')
        return render(request, 'register.html')



def logout(request):
        auth.logout(request)
        return redirect('/')



def form(request):
        if request.method == 'POST':
            name = request.POST.get('name')
            dob = request.POST.get('dob')
            age = request.POST.get('age')
            gender = request.POST.get('gender')
            phone = request.POST.get('phone')
            email = request.POST.get('email')
            address = request.POST.get('address')
            courses = request.POST.get('courses')
            department = request.POST.get('department')
            purpose = request.POST.get('purpose')
            materials = request.POST.getlist('materials')
            message = "Order Confirmed"
            return render(request, 'form.html', {'message': message})
        return render(request, 'form.html')

from django.shortcuts import render

# Create your views here.
