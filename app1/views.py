from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
def home(request):
    return HttpResponse("Hello, this is SNEHAL CHAVAN from T1 Batch and my prn is 1841012")
