from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def virat(request):
    return render(request,'virat_koli.html')
def maxwell(request):
    return HttpResponse("i am a hero")
