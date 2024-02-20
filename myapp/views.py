from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,"home.html")

def contact(request):
    return render(request,"Contact me.html")

def follow(request):
    return render(request,"Follow us.html")


