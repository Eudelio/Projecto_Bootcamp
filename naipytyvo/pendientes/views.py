from django.shortcuts import render
from .models import Info
# Create your views here.
def pagina_principal(request):
    return render(request, "index.html")

def servicios(request):
    datos = Info.objects.all()   #Consultamos nuestra base de datos
    datos_enviados={'datos': datos}
    print(datos_enviados)
    return render(request, "servicios.html",datos_enviados) #enviamos los datos a la pagina
