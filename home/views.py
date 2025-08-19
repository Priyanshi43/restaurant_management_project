from django.shortcuts import render

def about(request):
    return render(request,'about.html')

def homepage_view(request):
    return render(request, 'home.html')    