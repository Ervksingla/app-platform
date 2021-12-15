from django.shortcuts import render, HttpResponse

# Create your views here.
def index(request):
    return render(request, 'jsform.html')
    #return HttpResponse("hello ji ki haal chaal")

def about(request):
    return HttpResponse("I am from odhan haryana")