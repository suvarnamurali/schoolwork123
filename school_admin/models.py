from django.db import models

# Create your models here.
class Teacher(models.Model):
    teacher_name = models.CharField(max_length = 30) #charfiled-datatype as varchar(30)
    teacher_email = models.CharField(max_length = 40)
    teacher_qualification = models.CharField(max_length = 100)
    teacher_dob = models.CharField(max_length = 40)
    tea_experience = models.IntegerField()
    teacher_phone  = models.BigIntegerField()
    teacher_photo = models.ImageField(upload_to = 'teacher/')

class Adminlogin(models.Model):
    admin_uid = models.CharField(max_length = 30)
    admin_pswd = models.CharField(max_length = 40)
