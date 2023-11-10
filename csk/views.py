from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def dhoni(request):
    return render(request,"ms_dhoni.html")
def jadeja(request):
    return HttpResponse("i am the best bowler")