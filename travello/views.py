from django.shortcuts import render
from .models import Destination
# Create your views here.

def index(request):

    dest1 = Destination()
    dest1.name = "Cake1"
    dest1.img = "img1.jpg"


    dest2 = Destination()
    dest2.name = "Cake2"
    dest2.img = "img1.jpg"


    dest3 = Destination()
    dest3.name = "Cake3"
    dest3.img = "img1.jpg"

    dests = [dest1, dest2, dest3]
    return render(request, 'index.html', {'dests': dests})
