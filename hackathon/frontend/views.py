from django.shortcuts import render, HttpResponse

# Create your views here.
def index(request):
    return render(request, 'index.html')


def getInfo(request):
    return render(request, 'getInfo.html')

