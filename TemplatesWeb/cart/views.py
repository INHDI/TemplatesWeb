from django.shortcuts import render
from django.views import View
from .forms import CartForm
from home.models import LoaiSPModel
from django.http import HttpResponse
# Create your views here.

class CartView(View):
    def get(self,request):
        a = CartForm()
        c = LoaiSPModel.objects.all()
        return render(request, 'cart/cart.html',{'f':a,'danhmuc':c})
    def post(self,request):
        g = CartForm(request.POST)
        if g.is_valid():
            g.save()
            return HttpResponse('Lưu oke')
        else:
            return HttpResponse('Sai')

class Thankyou(View):
    def get(self,request):
        c = LoaiSPModel.objects.all()
        return render(request, 'cart/thankyou.html',{'danhmuc':c})