from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.

User = get_user_model()

class Complete_info(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    id_user = models.IntegerField()
    full_name = models.CharField(max_length=100, blank=True)
    complete_address = models.TextField(max_length=1000, blank=True)
    role = models.CharField(max_length=100, blank=True)
    department = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.user.username
    

class Schedule(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    id_user = models.IntegerField()
    staff_name = models.CharField(max_length=100, blank=True)
    day_scheduled = models.CharField(max_length=100, blank=True)
    time_scheduled = models.CharField(max_length=100, blank=True)
    department = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.user.username
    

class Department(models.Model):
    department_name = models.CharField(max_length=100, blank=True)
    date_created = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.department_name



