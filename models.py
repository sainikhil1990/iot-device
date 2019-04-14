from django.db import models

# Create your models here.
class user_info(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    dept = models.CharField(max_length=200)
    auth_level = models.CharField(max_length=200)
    email_id = models.CharField(max_length=200)

class user_logindetails(models.Model):
    user_name = models.CharField(max_length=200)
    password = models.CharField(max_length= 200)
class device_info(models.Model):
    device_id = models.CharField(max_length=200)
    device_name = models.CharField(max_length=200)
    temp = models.CharField(max_length = 200)
    date = models.CharField(max_length = 200)

class Sensor1(models.Model):
    name = models.CharField(max_length = 200)
    Value = models.CharField(max_length=200)
    Desc = models.CharField(max_length=200)
    time_stamp = models.CharField(max_length=200)

class Sensor2(models.Model):
    name = models.CharField(max_length = 200)
    Value = models.CharField(max_length=200)
    Desc = models.CharField(max_length=200)
    time_stamp = models.CharField(max_length=200)

class Sensor3(models.Model):
    name = models.CharField(max_length = 200)
    Value = models.CharField(max_length=200)
    Desc = models.CharField(max_length=200)
    time_stamp = models.CharField(max_length=200)


