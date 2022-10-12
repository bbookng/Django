from asyncio import ReadTransport
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Restaurant
from .forms import RestaurantForm
# Create your views here.

def index(request):
    restaurants = Restaurant.objects.all()
    context = {
        'restaurants': restaurants,
    }
    return render(request, "restaurants/index.html", context)

def detail(request, pk):
    detail = Restaurant.objects.get(pk=pk)
    context = {
        'detail': detail,
    }
    return render(request, 'restaurants/detail.html', context)

def create(request):
    if request.method == "POST":
        form = RestaurantForm(request.POST, request.FILES)
        if form.is_valid():
            restaurant = form.save()
            return redirect('restaurants:detail', restaurant.pk)
    else:
        form = RestaurantForm()
        
    context = {
        'form': form,
    }
    return render(request, 'restaurants/create.html', context)