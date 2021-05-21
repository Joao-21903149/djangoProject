from django.urls import path
from . import views

app_name = "website"

urlpatterns = [
    path('', views.home_page_view, name='home'),
    path('home2/', views.lista_page_view, name='lista'),
    path('home3/', views.sauda_page_view, name='saudar'),
]
