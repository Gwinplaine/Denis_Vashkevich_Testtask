"""DVscandiweb URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from .views import index, add_product, mass_delete, favourites, add_to_fav
from django.urls import path

urlpatterns = [
    path('', index, name='index'),
    path('add-product/', add_product, name='add-product'),
    path('mass_delete', mass_delete, name='mass-delete'),
    path('favourites/', favourites, name='favourites'),
    path('add_to_fav', add_to_fav, name='add_to_fav'),
]
