from django.urls import path
# from .views import index
from . import views

urlpatterns = [
    path('', views.index_page, name='index'),
    path('home/login' , views.login_page , name= 'login'),
    path('home/logout' , views.logout_page , name= 'logout'),
    path('home/register' , views.register , name='register')
] 