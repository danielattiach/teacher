from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.mail import send_mail
from django.contrib.auth.models import User
from .models import Contact

def send(request):
  if request.method == 'POST':
    name = request.POST.get('name', '')
    email = request.POST.get('email', '')
    phone = request.POST.get('phone', '')
    message = request.POST.get('message', '')
    subject = request.POST.get('subject', '')

    if request.user.is_authenticated:
      author = request.user.id
      author_name = User.objects.get(id=author).first_name + ' ' + User.objects.get(id=author).last_name
      teacher = User.objects.get(is_staff=True).id
      contact = Contact(name=name, email=email, phone=phone, message=message, subject=subject, author=author, author_name=author_name, target=teacher, target_name='Teacher')
    else:
      teacher = User.objects.get(is_staff=True).id
      contact = Contact(name=name, email=email, phone=phone, message=message, subject=subject, author=-1, author_name='Unregistered User', target=teacher, target_name='Teacher')
    
    contact.save()

    messages.success(request, 'תודה, נחזור אליכם בהקדם')

    send_mail(
        'PyTut',
        'Check your admin area, fam.',
        'daniel.coding.teacher@gmail.com',
        ['danielattiach@gmail.com'],
        fail_silently=False,
    )

    return redirect('/')

def delete_message(request):
  if request.method == "POST":
    if request.user.is_authenticated:
      msg_id = request.POST.get('msg_id', '')
      if Contact.objects.get(pk=msg_id).target == request.user.id:
        Contact.objects.filter(pk=msg_id).update(show_message=False)
        return redirect('/accounts/dashboard')
    else:
      return render(request, 'pages/index.html')

def reply_message(request, msg_id):
  if request.method == "POST":
    if request.user.is_authenticated:
      subject = request.POST.get('subject', '')
      message = request.POST.get('message', '')
      name = request.user.first_name + ' ' + request.user.last_name
      email = request.user.email
      author = request.user.id
      target = Contact.objects.get(pk=msg_id).author
      target_name = Contact.objects.get(pk=msg_id).author_name
      contact = Contact(name=name, email=email, message=message, subject=subject, author=author, author_name=name, target=target, target_name=target_name)
      contact.save()
      return redirect('/accounts/dashboard')
    else:
      return render(request, 'pages/index.html')

def teacher_message(request):
  if request.method == "POST":
    if request.user.is_authenticated:
      subject = request.POST.get('teacher-message-subject', '')
      message = request.POST.get('teacher-message-message', '')
      name =  request.user.first_name + ' ' + request.user.last_name
      email = request.user.email
      author = request.user.id
      teacher = User.objects.get(is_staff=True).id
      target_name = 'Teacher'
      contact = Contact(name=name, email=email, message=message, subject=subject, author=author, author_name=name, target=teacher, target_name=target_name)
      contact.save()
      return redirect('/accounts/dashboard')
    else:
      return render(request, 'pages/index.html')

def user_message(request):
  if request.method == "POST":
    if request.user.is_authenticated:
      subject = request.POST.get('user-message-subject', '')
      message = request.POST.get('user-message-message', '')
      username = request.POST.get('user-message-target', '')
      target_obj = User.objects.get(username=username)
      target = target_obj.id
      target_name = target_obj.first_name + ' ' + target_obj.last_name
      name =  request.user.first_name + ' ' + request.user.last_name
      email = request.user.email
      author = request.user.id
      contact = Contact(name=name, email=email, message=message, subject=subject, author=author, author_name=name, target=target, target_name=target_name)
      contact.save()
      return redirect('/accounts/dashboard')
    else:
      return render(request, 'pages/index.html')
