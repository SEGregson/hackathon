from sqlite3 import IntegrityError
from django.http import HttpResponse
from django.shortcuts import render
from rest_framework.response import Response
from .models import family
from django.core.files.storage import default_storage
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.views import APIView
from django.db.models import Q
import json

# Create your views here.

@api_view(["POST"])
def main(request):
    JSON = json.loads(request.body)
    total_user_budget = JSON['grocery_budget']+JSON['leisure_budget']+JSON['transport_budget']+JSON['accomodation_budget']

    budgeting = family.objects.filter(
        member_Count=JSON['member_Count'],
        dependants_Count=JSON['dependants_Count'],
        income_Per_Year=JSON['income_Per_Year'],
        number_Of_Pets=JSON['number_Of_Pets'])
    
    grocery_Budget = budgeting.grocery_Budget
    leisure_Budget = budgeting.leisure_Budget
    transport_Budget = budgeting.transport_Budget
    accomodation_Budget = budgeting.accomodation_Budget

    total_budget = grocery_Budget+leisure_Budget+transport_Budget+accomodation_Budget


    spending = None
    if total_user_budget < total_budget:
        spending = "Under-Spending"
    elif total_user_budget > total_budget:
        spending = "Over-Spending"
    elif total_user_budget == total_budget:
        spending = "Balanced-Spending"

    return Response({"spending": spending, 
            "GrocerySpendingDiff": JSON['grocery_budget']-grocery_Budget, 
            "LeisureSpendingDiff": JSON['leisure_budget']-leisure_Budget, 
            "TransportSpendingDiff": JSON['transport_budget']-transport_Budget,
            "AccomodationSpendingDiff": JSON['accomodation_budget']-accomodation_Budget},
            status=200)