from django.contrib import admin
from .models import Coin, Algo, Currency, Method, Reviews

@admin.register(Coin)
class CoinAdmin(admin.ModelAdmin):
    list_display = ('title','date_publ')

@admin.register(Algo)
class AlgoAdmin(admin.ModelAdmin):
    list_display = ('title', )

@admin.register(Currency)
class CurrencyAdmin(admin.ModelAdmin):
    list_display = ('title', )

@admin.register(Reviews)
class ReviewsAdmin(admin.ModelAdmin):
    list_display = ('name', 'coin')


@admin.register(Method)
class MethodAdmin(admin.ModelAdmin):
    list_display = ('title', )