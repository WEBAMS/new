from django.contrib import admin
from .models import Coin, Algo, Currency


@admin.register(Coin)
class CoinAdmin(admin.ModelAdmin):
    list_display = ('title','date_publ')