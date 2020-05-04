from django.urls import path
from . import views

urlpatterns = [

    path('index/', views.IndexView.as_view() ,name='index'),
    path('shop/',views.ShopView.as_view(),name='shop'),
    path('shop-single/',views.ShopsingleView.as_view(),name='shop_single'),


]

