from django.shortcuts import render
from django.shortcuts import render

def index(request):
    return render(request, "ejemplo/saludar.html")


from miproyecto.models import Exptedientes
