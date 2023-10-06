from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    return render(request,"second.html")
def rum(request):
     return render(request,"rum.html")
def beer(request):
     return render(request,"beer.html")
def gin(request):
     return render(request,"gin.html")
def brandy(request):
     return render(request,"brandy.html")
def vodka(request):
     return render(request,"vodka.html")
def whiskey(request):
     return render(request,"whiskey.html")
def tequila(request):
     return render(request,"tequila.html")
def login(request):
     return render(request,"login.html")
def sign_up(request):
     return render(request,"sign_up.html")
def about_us(request):
     return render(request,"about-us.html")

def courseDetails(request,courseID):
    return HttpResponse(courseID)
def courseList(request,courseName):
    return HttpResponse(courseName)    
