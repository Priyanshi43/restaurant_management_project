import requests
from django.shortcuts import render

def menu_home(request):
    api_url = 'http://localhost:800/api/menu/'
    try:
        response = request.get(api_url)
        menu_items = response = response.json()
    except:
        menu_items = []

    return render(request,'orders/menu_home.html',{'menu_items':menu_items})        