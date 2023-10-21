from django.db import models
from django.contrib.postgres import *
from datetime import datetime, timedelta
from django.utils import timezone


class family(models.Model):
    family_Id           = models.AutoField(primary_key=True)
    income_Per_Year     = models.FloatField(null=True)
    member_Count        = models.IntegerField(null=True)
    dependents_Count    = models.IntegerField(null=True)
    location            = models.CharField(choices=(('London', 'London'),('Midlands', 'Midlands'),('North', 'North'),('South', 'South')), max_length=100, null=True)
    budget_Week         = models.FloatField()
    budget_Month        = models.FloatField()
    budget_Year         = models.FloatField()
    grocery_Budget      = models.FloatField()
    leisure_Budget      = models.FloatField()
    transport_Budget    = models.FloatField()
    accomodation_Budget = models.FloatField()
    savings_Budget      = models.FloatField()

    def __str__(self):
        return (f"{self.member_Count}M-{self.number_Of_Boys}M-{self.number_Of_Girls}-F{self.number_Of_Babies}B")

    def disposable_Income(self):
        if self.income_Per_Year <= 12570:
            return (self.income_Per_Year)
        elif self.income_Per_Year < 12570 and self.income_Per_Year <= 50270:
            return (self.income_Per_Year - (self.income_Per_Year * 0.2))
        elif self.income_Per_Year < 50270 and self.income_Per_Year <= 125140:
            return (self.income_Per_Year - (self.income_Per_Year * 0.4))
        elif self.income_Per_Year < 125140:
            return (self.income_Per_Year - (self.income_Per_Year * 0.45))
        
    def income_Per_Month(self):
        return (self.income_Per_Year / 12)
        
    def income_Per_Week(self):
        return (self.income_Per_Year / 52)
    
    def income_Per_Child(self):
        return (self.income_Per_Year / (self.member_Count - 2))
    
    def retained_Income(self):
        return (self.family_Id.disposable_Income() - self.budget_Year)
