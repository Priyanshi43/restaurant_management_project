from django.urls import path
from .views import *

urlpatterns = [
    path('about/', veiws.about, name='about'),
]