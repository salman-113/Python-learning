from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):

    # person = {
    #     'name' : 'Salman',
    #     'age' : 20,
    #     'place' : 'Calicut'
    # }

    numbers = {
        'num1' : 10
    }
    return render(request, 'index.html', numbers)

def about(request):
    return render(request, 'about.html')

def booking(request):
    return render(request, 'booking.html')

def doctors(request):
    return render(request, 'doctors.html')

def contact(request):
    return render(request, 'contact.html')

def department(request):
    return render(request, 'department.html')