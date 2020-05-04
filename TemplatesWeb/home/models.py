from django.db import models

# Create your models here.


class LoaiSPModel(models.Model):
    Ma_loai = models.CharField(max_length=10, verbose_name='Mã Loại Sản Phẩn', blank=True,)
    Loai_sp = models.CharField(max_length=50, verbose_name='Tên Loại Sản Phẩn', blank=True,)
    Mo_ta = models.TextField(verbose_name='Mô Tả')

    def __str__(self):
        return self.Loai_sp


class SanPhamModel(models.Model):
    Loai_sp = models.ForeignKey(LoaiSPModel,on_delete=models.CASCADE,default=1,verbose_name='Loại Sản Phẩm')
    Ma_sp = models.CharField( max_length=10, verbose_name='Mã Sản Phẩm')
    Ten_sp = models.CharField(max_length=50, verbose_name='Tên Sản Phẩm', blank=True)
    Mo_ta = models.TextField(verbose_name='Mô Tả')
    Gia_nhap = models.IntegerField(verbose_name='Giá Nhập', blank=True, default=0)
    Anh = models.ImageField(upload_to='static\home\images')

    def __str__(self):
        return self.Ten_sp


mota= ((1,'Đang Sale 10 %'),(2,'Đang giảm mạnh'),(3,'Đang Sale 50 %'))

class SPBanModel(models.Model):
    San_Pham = models.ForeignKey(SanPhamModel,on_delete=models.CASCADE)
    Loai_sp = models.ForeignKey(LoaiSPModel,on_delete=models.CASCADE)
    Mo_ta = models.SmallIntegerField(verbose_name='Mô Tả',choices =mota,default=2 )
    Gia_ban = models.IntegerField(verbose_name='Giá Bán', blank=True, default=200000)
    Gia_sale = models.IntegerField(verbose_name='Giá Sale',  default=150000)
    Hang_ton = models.IntegerField(verbose_name='Hàng Tồn', default=100)

    def __str__(self):
        return self.San_Pham.Ten_sp