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
    target_form = request.POST.get('target_form', '')
    print(request.POST)

    if request.user.is_authenticated:
      if target_form:
        author = request.user.id
        author_name = User.objects.get(id=author).first_name + ' ' + User.objects.get(id=author).last_name

        target = User.objects.get(username=target_form).id
        target_name = User.objects.get(id=target).first_name + ' ' + User.objects.get(id=target).last_name
        contact = Contact(name=name, email=email, phone=phone, message=message, subject=subject, author=author, target=target, target_name=target_name, author_name=author_name)
      else:
        author = request.user.id
        author_name = User.objects.get(id=author).first_name + ' ' + User.objects.get(id=author).last_name
        admin = User.objects.get(is_staff=True).id
        contact = Contact(name=name, email=email, phone=phone, message=message, subject=subject, author=author, author_name=author_name, target=admin, target_name='Admin')
    else:
      admin = User.objects.get(is_staff=True).id
      contact = Contact(name=name, email=email, phone=phone, message=message, subject=subject, author=-1, author_name='Unregistered User', target=admin, target_name='Admin')
    
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