from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib import messages, auth
from django.http import JsonResponse
from contact.models import Contact
from django.conf import settings
from .models import Avatar
import os

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
      messages.error(request, 'הסיסמאות מוכרחות להיות זהות')
      return render(request, 'accounts/register.html')
  else:
    if request.user.is_authenticated:
      return redirect('/')
  return render(request, 'accounts/register.html')

def login(request):
  if request.method == 'POST':
    username = request.POST['username']
    password = request.POST['password']

    user = auth.authenticate(username=username, password=password)

    if user is not None:
      auth.login(request, user)
      return redirect('dashboard')
    else:
      messages.error(request, 'הפרטים שהזנת אינם נכונים')
      return render(request, 'accounts/login.html')
  else:
    if request.user.is_authenticated:
      return redirect('/')
    return render(request, 'accounts/login.html')

def logout(request):
  if request.method == 'POST':
    auth.logout(request)
    return redirect('index')

def dashboard(request):
  if request.user.is_authenticated:
    try:
      avatar = Avatar.objects.get(user_id=request.user.id)
    except:
      avatar = None
    messages = Contact.objects.filter(target=request.user.id, show_message=True).order_by('-contact_date')
    if avatar:
      context = {
        'messages': messages,
        'avatar': avatar.avatar.url,
      }
    else:
      context = {
        'messages': messages,
        'avatar': '/media/avatars/no-avatar.png',
      }
  else:
    context = {
      'messages': 'Login to unlock this feature'
    }
  return render(request, 'accounts/dashboard.html', context)

def message(request, message_id):
  if request.user.is_authenticated:
    msg = get_object_or_404(Contact, pk=message_id)
    try:
      sender_avatar = Avatar.objects.get(user_id=msg.author)
    except:
      sender_avatar = None
    if msg.target == request.user.id:
      if sender_avatar:
        context = {
          'message': msg,
          'sender': sender_avatar.avatar.url,
        }
      else:
        context = {
          'message': msg,
          'sender': '/media/avatars/no-avatar.png',
        }
      return render(request, 'accounts/message.html', context)
    else:
      return redirect('/')
  else:
    return redirect('/')

def upload_avatar(request):
    if request.user.is_authenticated:
      if request.method == 'POST':
        try:
          current_avatar = Avatar.objects.get(user_id=request.user.id)
        except:
          current_avatar = None
        avatar_image = request.FILES.get('avatar', '')
        if avatar_image.seek(0, os.SEEK_END) > 1000000:
          try:
            avatar = Avatar.objects.get(user_id=request.user.id)
          except:
            avatar = None
          messages = Contact.objects.filter(target=request.user.id, show_message=True).order_by('-contact_date')
          if avatar:
            context = {
              'messages': messages,
              'avatar': avatar.avatar.url,
              'alert': 'גודל הקובץ המקסימלי הוא 1 מגה בייט'
            }
          else:
            context = {
              'messages': messages,
              'avatar': '/media/avatars/no-avatar.png',
              'alert': 'גודל הקובץ המקסימלי הוא 1 מגה בייט'
            }
          return render(request, 'accounts/dashboard.html', context)
        if current_avatar:
          os.remove(settings.MEDIA_ROOT+current_avatar.avatar.url[6:])
          current_avatar.delete()
          avatar_instance = Avatar(user_id=request.user.id, avatar=avatar_image)
          avatar_instance.save()
        else:
          avatar_instance = Avatar(user_id=request.user.id, avatar=avatar_image)
          avatar_instance.save()
      return redirect('/accounts/dashboard')
    else:
      return redirect('/')

def search_user(request):
  username = request.GET.get('username')
  users = [user.username for user in User.objects.filter(username__contains=username)] if username else None
  return JsonResponse({'users': users})