from django.http import HttpResponse
from django.shortcuts import render
from datetime import datetime


def home_page_view(request):
    context = {
        'now': datetime.now()
    }
    return render(request, "website/home.html")


def lista_page_view(request):
    context = {
        'lista': ["django", "python"]
    }

    return render(request, "website/home2.html", context)


def sauda_page_view(request):
    # return HttpResponse(f'Olá, {name.capitalize()} 😀!. São {context} horas', "website/home3.html")
    return HttpResponse("<h1>Bom dia</h1>")
