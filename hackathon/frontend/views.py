from django.shortcuts import render, HttpResponse

# Create your views here.
def index(request):
    return render(request, 'index.html')


def getInfo(request):
    return render(request, 'getInfo.html')

def output(request):
    return render(request, 'output.html')

def underspending(request):
    return render(request, 'underspending.html')
