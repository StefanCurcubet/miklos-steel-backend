from django.urls import path
from . import views

urlpatterns = [
    path('getProducts/', views.getAllProducts),
    path('addToBasket/', views.createBasketItem),
    path('removeBasketItem/<str:pk>', views.removeBasketItem),
    path('getBasketItems/', views.getBasketItems),
    path('buyBasket/', views.buyBasket),
]

