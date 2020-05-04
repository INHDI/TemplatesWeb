from django.urls import path
from . import views

urlpatterns = [

    path('cart/', views.CartView.as_view(), name='cart'),
    path('thankyou/', views.Thankyou.as_view()),

]
