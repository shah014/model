from django.db import models

# Create your models here.


class Subject(models.Model):
    sub_code = models.PositiveIntegerField()
    sub_name = models.CharField(max_length=50)
    sub_writer = models.CharField(max_length=50)
    sub_price = models.PositiveIntegerField()

    def __str__(self):
        return self.sub_name


class Teacher(models.Model):
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=50)
    salary = models.PositiveIntegerField()
