from django.shortcuts import render, redirect
from django.contrib import messages, auth
from django.contrib.auth.models import User

def register(request):
  if request.method == 'POST':
    # Get form values
    first_name = request.POST['first_name']
    last_name = request.POST['last_name']
    username = request.POST['reg_username']
    email = request.POST['reg_email']
    password = request.POST['reg_password'] 
    password2 = request.POST['reg_password2']

    # Check if passwords match
    if password == password2:
      # Check username
      if User.objects.filter(username=username).exists():
        messages.error(request, 'That username is already taken')
        return redirect('register')
      else:
        # Check email
        if User.objects.filter(email=email).exists():
          messages.error(request, 'That email is being used')
          return redirect('register')
        else:
          user = User.objects.create_user(username=username, password=password, email=email, first_name=first_name, last_name=last_name)
          # Login after register
          auth.login(request, user, backend='django.contrib.auth.backends.ModelBackend')
          messages.success(request, f'{user} ,ברוכים הבאים')
          return redirect('index')
    else:
      messages.error(request, 'Passwords must match')
      return redirect('index')
  return render(request, 'index')

def login(request):
  if request.method == 'POST':
    username = request.POST['username']
    password = request.POST['password']

    user = auth.authenticate(username=username, password=password)

    if user is not None:
      auth.login(request, user)
      return redirect('dashboard')
    else:
      messages.error(request, 'Invalid credentials')
      return redirect('index')
  else:
    return render(request, 'index')

def logout(request):
  if request.method == 'POST':
    auth.logout(request)
    return redirect('index')

def dashboard(request):
  return render(request, 'accounts/dashboard.html')