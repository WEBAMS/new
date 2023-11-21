from django.urls import path
from . import views

urlpatterns = [
    path('', views.CoinsViews.as_view(), name='home'),
    path('<slug:slug>/', views.CoinDetail.as_view(), name='coin_detail'),
    path('reviews/<int:pk>', views.AddReview.as_view(), name='add_review')
]