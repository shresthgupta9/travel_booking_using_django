from django.shortcuts import render
from datetime import datetime
from home.models import Feedback
from home.models import Book
from django.contrib import messages

# Create your views here.

def index(request):
    return render(request, 'index.html')

def tandc(request):
    return render(request, 'tandc.html')

def support(request):
    return render(request, 'support.html')

def book(request):
    if request.method == "POST":
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        car = request.POST.get('car')
        date = request.POST.get('date')
        month = request.POST.get('month')
        year = request.POST.get('year')
        fromm = request.POST.get('fromm')
        to = request.POST.get('to')
        book = Book(name=name, phone=phone, car=car, date=date, month=month, year=year, fromm=fromm, to=to, logged_date=datetime.today())
        book.save()
        messages.success(request, "Your booking has been submitted")
    return render(request, 'book.html')

def feedback(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        rate = request.POST.get('rate')
        content = request.POST.get('content')
        feedback = Feedback(name=name, email=email, rate=rate, content=content, date=datetime.today())
        feedback.save()
        messages.success(request, "Your feedback has been submitted")
    return render(request, 'feedback.html')