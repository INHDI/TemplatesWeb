from django.urls import path
from . import views

urlpatterns = [

    path('index/', views.IndexView.as_view(), name='index'),
    path('shop/', views.ShopView.as_view(), name='shop'),
    path('home/sanpham/chitiet/<int:id>', views.chitietsp),
    path('home/sanpham/<int:id>', views.loaisp, name='sanpham'),

]
