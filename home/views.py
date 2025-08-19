from django.shortcuts import render

def about(request):
    return render(request,'about.html')

def homepage_view(request):
    context = {
        "phone": settings.RESTAURANT_PHONE   
    }
    return render(request, 'home.html')    

def menu(request):
    menu_items = [
        {"name": "Pizza","Price": "200"},
        {"name": "Burger", "Price": "100"},
        {"name": "Pasta", "Price": "150"},
        {"name": "Coffee", "Price": "80"},
    ]    
    return render(request, "menu.html", {"menu_items": menu_items})