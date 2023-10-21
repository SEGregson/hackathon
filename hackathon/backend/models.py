from django.db import models
from django.contrib.postgres import *
from datetime import datetime, timedelta
from django.utils import timezone


class family(models.Model):
    family_Id = models.AutoField(primary_key=True)
    member_Count = models.IntegerField()
    dependents_Count = models.IntegerField()
    number_Of_Boy

    def __str__(self):
        return (f"{}")     


class budget(models.Model):
    budget_Id = models.AutoField(primary_key=True)
    family_Id = models.ForeignKey(family, on_delete=models.CASCADE)
    budget_Name = models.CharField(max_length=50)
    budget_Amount = models.IntegerField()
    budget_Start_Date = models.DateField()
    budget_End_Date = models.DateField()

    def __str__(self):
        return self.budget_Name      