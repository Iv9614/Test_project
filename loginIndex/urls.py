from django.urls import path
# from .views import index
from . import views

urlpatterns = [
    path('', views.index_page, name='index'),
    path('register' , views.sign_up , name='register')
]