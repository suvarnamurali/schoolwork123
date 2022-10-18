from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,'common/home.html')

def a_login(request):
    return render(request,'common/a_login.html')

def s_login(request):
    return render(request,'common/s_login.html')

def t_login(request):
    return render(request,'common/t_login.html')