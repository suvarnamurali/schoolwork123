# Generated by Django 4.1 on 2022-10-18 05:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('teacher_name', models.CharField(max_length=30)),
                ('teacher_email', models.CharField(max_length=40)),
                ('teacher_address', models.CharField(max_length=100)),
                ('teacher_qualification', models.CharField(max_length=100)),
                ('teacher_gender', models.CharField(max_length=10)),
                ('teacher_dob', models.CharField(max_length=40)),
                ('teacher_experience', models.IntegerField()),
                ('teacher_phone', models.BigIntegerField()),
                ('teacher_password', models.CharField(max_length=40)),
                ('teacher_photo', models.ImageField(upload_to='teacher/')),
            ],
        ),
    ]
