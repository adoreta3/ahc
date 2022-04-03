from unicodedata import name
from django.shortcuts import render
from .models import Customer


def index(request):
    if request.method == 'POST':
        print(request.POST.get)
        Customer.objects.create(name=request.POST.get('name'), service=request.POST.get('service'), phone=request.POST.get('mobile'))
        return render(request, 'index.html')
    return render(request, 'index.html')