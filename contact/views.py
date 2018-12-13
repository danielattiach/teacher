from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.mail import send_mail
from .models import Contact

def send(request):
  if request.method == 'POST':
    name = request.POST['name']
    email = request.POST['email']
    phone = request.POST['phone']
    message = request.POST['message']
    subject = request.POST['subject']

    contact = Contact(name=name, email=email, phone=phone, message=message, subject=subject)

    contact.save()

    messages.success(request, 'Your message has been submitted, you will be contacted shortly.')

    send_mail(
        'PyTut',
        'Check your admin area, fam.',
        'daniel.coding.teacher@gmail.com',
        ['danielattiach@gmail.com'],
        fail_silently=False,
    )

    return redirect('/')