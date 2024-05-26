from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def home(request):
    print(request)
    return HttpResponse("Hello welcome back home")
