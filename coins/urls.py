from django.urls import path
from . import views

urlpatterns = [
    path('', views.CoinsViews.as_view()),
    path('<slug:slug>/', views.CoinDetail.as_view())
]