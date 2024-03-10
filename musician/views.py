from django.shortcuts import render

# Create your views here.

def add_musician(request):
    return render(request,'musician.html')