from django.http import request
from  django.shortcuts import render,HttpResponse
from django.contrib.auth.forms import UserCreationForm

def index_page (request):
    return render(request , 'loginIndex/Home.html')

def login_page(request):
    return render(request ,'loginIndex/login.html' )

def logout_page(request):
    return render(request ,'loginIndex/logout.html' )

def register(request):
    return render(request ,'loginIndex/register.html' )

   
def sign_up (request):
    form = UserCreationForm()
    context  ={
        'form' :form
    }

    return render(request , 'loginIndex/register.html')