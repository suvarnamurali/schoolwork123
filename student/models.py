from django.db import models

# Create your models here.

class Studentlogin(models.Model):
    student_id = models.CharField(max_length = 30)
    student_pwd = models.CharField(max_length = 40)
