from django.shortcuts import render, redirect
from django.http import HttpResponse

def index(request):
  return render(request, 'pages/index.html')

def barak(request):
  return render(request, 'pages/barak.html')