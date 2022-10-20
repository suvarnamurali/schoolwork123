from django.db import models

# Create your models here.

class Teacherlogin(models.Model):
    teacher_id = models.CharField(max_length = 30)
    teacher_pwd = models.CharField(max_length = 40)

