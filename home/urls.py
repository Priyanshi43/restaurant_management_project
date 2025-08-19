from django.urls import path
from .views import *

urlpatterns = [
    path('about/', veiws.about, name='about'),
    path('contact/', views.contact_us, name='contact'),
]