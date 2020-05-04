from django.shortcuts import render
from django.views import View 
from django.http import HttpResponse
# Create your views here.

class IndexView(View):
    def get(self,request):
        #a = SPBanModel.objects.all()
        #c= LoaiSPModel.objects.all()
        return render(request, 'home/index.html')


class ShopView(View):
    def get(self,request):
        return render(request, 'home/shop.html')

class ShopsingleView(View):
    def get(self,request):
        return render(request, 'home/shop-single.html')