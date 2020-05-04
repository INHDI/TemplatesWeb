from django.db import models
from home.models import SPBanModel
# Create your models here.

class Cart(models.Model):
    Ho_ten = models.CharField(max_length=50, verbose_name='Họ Và Tên', blank=True)
    SDT = models.CharField(max_length=50, verbose_name='Số Điện thoại', blank=True)
    Email = models.EmailField(blank=True)
    Dia_chi = models.CharField(max_length=500,blank=True,verbose_name='Địa chỉ')
    Ghi_chu = models.CharField(max_length=500,verbose_name='Ghi Chú')
    So_luong = models.PositiveSmallIntegerField(max_length=5,verbose_name='Số lượng',default=1, blank=True)
    San_Pham = models.ForeignKey(SPBanModel, on_delete=models.CASCADE)

    def __str__(self):
        return self.Ho_ten