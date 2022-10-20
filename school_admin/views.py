from django.shortcuts import render
from .models import Teacher

# Create your views here.
def a_home(request):
    return render(request,'school_admin/a_home.html')

def add_tr(request):
    if request.method == 'POST':
        t_name = request.POST['t_name']
        t_email = request.POST['t_email']
        t_qul = request.POST['t_qul']
        t_dob = request.POST['t_dob']
        t_phn = request.POST['t_phn']
        t_pic = request.FILES['t_pic']
        t_exp = request.POST['t_exp']
        teacher = Teacher(teacher_name = t_name,teacher_email = t_email,teacher_qualification = t_qul,teacher_dob = t_dob,teacher_phone = t_phn,
        teacher_photo = t_pic,tea_experience = t_exp)
        teacher.save()
       


    return render(request,'school_admin/add_teacher.html')

def view_st(request):
    return render(request,'school_admin/view_student.html')

def view_tr(request):
    return render(request,'school_admin/view_teachers.html')

def chg_pwd(request):
    return render(request,'school_admin/change_password.html')