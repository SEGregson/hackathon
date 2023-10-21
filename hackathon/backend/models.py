from django.db import models
from django.contrib.postgres import *
from datetime import datetime, timedelta
from django.utils import timezone


class family(models.Model):
    family_Id = models.AutoField(primary_key=True)
    income = models.FloatField(null=True)
    member_Count = models.IntegerField(null=True)
    dependents_Count = models.IntegerField(null=True)
    number_Of_Boys = models.IntegerField(null=True)
    number_Of_Girls = models.IntegerField(null=True)
    number_Of_Babies = models.IntegerField(null=True)

    def __str__(self):
        return (f"{self.member_Count}M-{self.number_Of_Boys}M-{self.number_Of_Girls}-F{self.number_Of_Babies}B")     


class budget(models.Model):
    budget_Id = models.AutoField(primary_key=True)
    family_Id = models.ForeignKey(family, on_delete=models.CASCADE)
    budget_Week = models.FloatField()
    budget_Month = models.FloatField()
    budget_Year = models.FloatField()
    


    def __str__(self):
        return self.family_Id      