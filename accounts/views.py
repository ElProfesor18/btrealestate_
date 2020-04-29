from django.shortcuts import render, redirect
from django.contrib import messages, auth
from django.contrib.auth.models import User

# Create your views here.
def register(request):
    if request.method == "POST":
        
        # Taking Input
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']

        if password == password2:
            # Check Username
            if User.objects.filter(username=username).exists():
                messages.error(request, 'Username Already Taken!')

                return redirect('register')

            # Check Email
            elif User.objects.filter(email=email).exists():
                messages.error(request, 'Email Already Taken!')

                return redirect('register')
            
            else :
                # Looks Good
                user = User.objects.create_user(username=username, email=email, password=password, first_name=first_name, last_name=last_name)
                user.save()
                messages.success(request, 'You are now registered and can login')

                return redirect('login')


        else:
            messages.error(request, "Passwords Don't Match!")
            return redirect('register')
    
    else:
        return render(request, 'accounts/register.html', {})

def login(request):
    if request.method == "POST":
        
        username = request.POST['username']
        password = request.POST['password']
        
        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            messages.success(request, 'You ar now logged in.')
            return redirect('dashboard')
        
        else:
            messages.error(request, 'Invalid Credentials!')
            return redirect('login')
    
    else:
        return render(request, 'accounts/login.html', {})

def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        messages.success(request, 'You are logged out!')
        return redirect('index')
    # return redirect(request, 'index', {})

def dashboard(request):
    return render(request, 'accounts/dashboard.html', {})