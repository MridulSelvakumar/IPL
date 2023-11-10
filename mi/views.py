from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def rohit(request):
    return render(request,'rohit_sharma.html')
def bomra(request):
    return HttpResponse("hi i am a bowler")
