from django.shortcuts import render
import random

# Create your views here.
def lotto(request):
    no = random.sample(range(1, 999), 1)
    answer = random.sample(list(range(1, 45)), 6)
    context = {
        'no' : no,
        'answer': answer,
    }
    return render(request, 'lotto.html', context)