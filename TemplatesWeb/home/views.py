from django.shortcuts import render
from django.views import View 
from django.http import HttpResponse
from .models import SPBanModel,LoaiSPModel
# Create your views here.

class IndexView(View):
    def get(self,request):
        a = SPBanModel.objects.all()
        c= LoaiSPModel.objects.all()
        return render(request, 'home/index.html',{'f':a,'danhmuc':c})


class ShopView(View):
    def get(self,request):
        a = SPBanModel.objects.all()
        c= LoaiSPModel.objects.all()
        return render(request, 'home/shop.html',{'f':a,'danhmuc':c})


def chitietsp(request,id):
    c = LoaiSPModel.objects.all()
    chitietsp = SPBanModel.objects.all().filter(id=id)
    return render(request,'home/shop-single.html',{'a':chitietsp,'b':c,'danhmuc':c})


def loaisp(request,id):
    c = LoaiSPModel.objects.all()
    danhmuc= SPBanModel.objects.all().filter(Loai_sp_id=id)
    return render(request,'home/phanloai.html',{'a':danhmuc,'b':c,'danhmuc':c})

