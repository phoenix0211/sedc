from django.db import models
import os

# to link the database run the following commands
# python manage.py makemigrations about
# python manage.py sqlmigrate about 0001
# python manage.py migrate
# python manage.py shell


def get_image_path(instance, filename):
    return os.path.join('student', str(instance.UIN), filename)


class Student(models.Model):
    UIN = models.BigIntegerField(primary_key=True)
    Name = models.CharField(max_length=50)
    F_name = models.CharField(max_length=50)
    M_name = models.CharField(max_length=50)
    Contact = models.CharField(max_length=10)
    EmailId = models.CharField(max_length=50)
    DateofBirth = models.DateField()
    Link = models.CharField(max_length=10000)
    sec_ans = models.CharField(max_length=50, default="None")
    password = models.CharField(max_length=50, default="password")
    images = models.ImageField(upload_to=get_image_path, default="a")

    def __str__(self):
        return str(self.UIN)