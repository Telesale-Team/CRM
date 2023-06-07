from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Category (models.Model):
    
    name = models.CharField('ชื่อหมวดหมู่',max_length=60)
    class Meta:

        verbose_name_plural = "Create Category"
        verbose_name = "Category"
    
    def __str__(self) :
        return self.name


    
class Stock (models.Model):
    
    name = models.CharField('ชื่อสินค้า',max_length=60,null=True)
    serial = models.CharField("รหัสสินค้า",max_length=60,null=True)
    quatity = models.PositiveIntegerField('จำนวน',default=0)
    detail = models.TextField('อุปกรณ์เสริม',max_length=255,null=True)
    category = models.ForeignKey(Category,on_delete=models.CASCADE,null=True)
    user_account = models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    date = models.DateTimeField('วันที่',auto_now_add=True,null=True,blank=True)

    status_item = models.TextChoices("สถานะการใช้งาน", "ใช้งานได้ ชำรุด")
    item_status = models.CharField(blank=True, choices=status_item.choices, max_length=100,default="ใช้งานได้")

    status_stock = models.TextChoices("สถานะคงคลัง", "สต๊อก ยืม")
    stock_status = models.CharField(blank=True, choices=status_stock.choices, max_length=100,default="สต๊อก")

    class Meta:

        verbose_name_plural = "Stock"
        verbose_name = "Item"

    def __str__(self):
        return self.name
    

#การใช้งาน Choices Modals
class Runner(models.Model):
    
    MedalType = models.TextChoices("MedalType", "GOLD SILVER BRONZE")
    name = models.CharField("person's first name",max_length=60)
    medal = models.CharField(blank=True, choices=MedalType.choices, max_length=10)
    

    def __str__(self):
        return self.name


