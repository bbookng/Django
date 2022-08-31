from django.shortcuts import render
import random

# Create your views here.
def dinner(request, menus, peoples):
    context = {
        'menus' : menus,
        'peoples' : peoples,
    }
    return render(request, 'dinner.html', context)