from django.shortcuts import render,redirect
from school_admin . models import Adminlogin
from student . models import Studentlogin
from teacher . models import Teacherlogin

# Create your views here.
def home(request):
    return render(request,'common/home.html')

def a_login(request):
    if request.method == 'POST':
        user_id = request.POST['a_usid']
        password = request.POST['a_pass']
        try:
            a_login = Adminlogin.objects.get(admin_uid = user_id,admin_pswd = password)
            return redirect('school_admin:hom')
        except:
            msg = "incorrect password and username"
            return render(request,'common/a_login.html',{"error_message":msg})
    return render(request,'common/a_login.html')

def s_login(request):
    if request.method == 'POST':
        s_id = request.POST['s_usid']
        s_password = request.POST['s_pass']
        try:
            s_login = Studentlogin.objects.get( student_id = s_id,student_pwd = s_password)
            return redirect('student:hom')
        except:
            msg = "incorrect password and username"
            return render(request,'common/s_login.html',{"error_message":msg})
    return render(request,'common/s_login.html')

def t_login(request):
    if request.method == 'POST':
        teacher_id = request.POST['tea_id']
        t_password = request.POST['t_pass']
        try:
            t_login = Teacherlogin.objects.get( teacher_id = teacher_id,teacher_pwd = t_password)
            return redirect('teacher:hom')
        except:
            msg = "incorrect password and username"
            return render(request,'common/t_login.html',{"error_message":msg})
    return render(request,'common/t_login.html')

   