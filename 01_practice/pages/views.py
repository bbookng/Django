from django.shortcuts import render
from random import sample
import requests

# Create your views here.
def lotto(request):
    URI = "https://www.dhlottery.co.kr/common.do?method=getLottoNumber&drwNo=1"
    lucky = requests.get(URI).json()
    answer = set()
    for i in range(1, 7):
        answer.add(lucky[f'drwtNo{i}'])
    bonus = lucky['bnusNo']
    
    result = [0] * 6
    for i in range(1000):
        tmp = set(sample(set(range(1, 46)), 6))
        n = answer & tmp
        if len(n) == 6:
            result[0] += 1
        elif len(n) == 5 and bonus in tmp:
            result[1] += 1
        elif len(n) == 5:
            result[2] += 1
        elif len(n) == 4:
            result[3] += 1
        elif len(n) == 3:
            result[4] += 1
        else:
            result[5] += 1
    
    context = {
        'data': result,
        'answer': list(answer),
        'bonus': bonus,
    }
    
    return render(request, 'lotto.html', context)