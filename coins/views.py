from django.shortcuts import render, redirect
from django.views.generic.base import View
from .models import Coin
from .form import ReviewForm

class CoinsViews(View):
    '''Список монет'''
    def get(self, request):
        coins = Coin.objects.all()
        return render(request, 'coins/coin.html', {'coin_list': coins})

class CoinDetail(View):
    '''Представление одной монеты'''
    def get(self, request, slug):
        coin = Coin.objects.get(url=slug)
        return render(request, 'coins/coin_detail.html', {'coin': coin})

class AddReview(View):
    '''Добавление отзыва'''
    def post(self, request, pk):
        form = ReviewForm(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            form.coin_id = pk
        return redirect('/')

