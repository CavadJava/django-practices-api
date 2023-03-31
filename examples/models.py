from django.shortcuts import render

# Create your views here.
from django.db import models


# Create your models here.
class FoodDb(models.Model):
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=500)

    @classmethod
    def create(cls, name, description):
        foodDb = cls(name=name, description=description)
        # do something with the book
        return foodDb


class StudentTest(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=30)

    class Meta:
        db_table = "student"


class Employee(models.Model):
    eid      = models.CharField(max_length=20)
    ename    = models.CharField(max_length=100)
    econtact = models.CharField(max_length=15)
    class Meta:
        db_table = "employee"