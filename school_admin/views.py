from django.shortcuts import render

# Create your views here.
def a_home(request):
    return render(request,'school_admin/a_home.html')

def add_tr(request):
    return render(request,'school_admin/add_teacher.html')

def view_st(request):
    return render(request,'school_admin/view_student.html')

def view_tr(request):
    return render(request,'school_admin/view_teachers.html')

def chg_pwd(request):
    return render(request,'school_admin/change_password.html')