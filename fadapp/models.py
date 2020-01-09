from django.db import models

# Create your models here.

class Userlogin(models.Model):
    username = models.CharField(max_length=30)
    password = models.CharField(max_length=30)
    role = models.CharField(max_length=30)


class Userdetails(models.Model):
    firstname = models.CharField(max_length=30)
    lastname = models.CharField(max_length=30)
    dob = models.DateField()
    gender = models.CharField(max_length=30)
    mobile = models.IntegerField()
    fk_login = models.ForeignKey(Userlogin, on_delete=models.CASCADE)
        

class Designerdetails(models.Model):
    boutiquename = models.CharField(max_length=30)
    qualification = models.CharField(max_length=50)
    about = models.TextField()
    fk_login = models.ForeignKey(Userlogin, on_delete=models.CASCADE)


class DesginerFabrics(models.Model):
    fabric_name = models.CharField(max_length=25)
    fabric_desc = models.TextField()
    fabric_cost = models.CharField(max_length=10)
    fabric_image = models.FileField(upload_to='images/')
    fk_login = models.ForeignKey(Designerdetails, on_delete=models.CASCADE)


class DesginerWorks(models.Model):
    work_image = models.FileField(upload_to='images/')
    work_title = models.CharField(max_length=25)
    work_desc = models.TextField()
    fk_login = models.ForeignKey(Designerdetails, on_delete=models.CASCADE)
