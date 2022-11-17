from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def function(request):
    return render(request,'index.html')


def func(request):
    email=request.GET['email']
    password=request.GET['pass']

    return HttpResponse(f'email of student is {email}<br> password is={password}')