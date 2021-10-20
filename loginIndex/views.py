from django.http import request
from  django.shortcuts import render,HttpResponse
from django.contrib.auth.forms import UserCreationForm

def index_page (request):
    return render(request , 'loginIndex/index.html')

def sign_up (request):
    form = UserCreationForm()
    context  ={
        'form' :form
    }

    return render(request , 'loginIndex/register.html')