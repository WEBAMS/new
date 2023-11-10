from django.shortcuts import render
from django.views.generic.base import View
from .models import Coin

class CoinsViews(View):
    '''Список монет'''
    def get(self, request):
        coins = Coin.objects.all()
        return render(request, 'coins/coin.html', {'coin_list': coins})
