from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Web (models.Model):
    name = models.CharField('เว็บไซต์ทำการตลาด',max_length=255)
    
    
    def __str__(self):
        return self.name

class Source (models.Model):
    name = models.CharField('ที่มาของลูกค้า',max_length=255)
    
    
    def __str__(self):
        return self.name
    
    
class Interest (models.Model):
    name = models.CharField('ความสนใจของลูกค้า',max_length=255)
    
    def __str__(self):
        return self.name
   
class Age (models.Model):
    name = models.CharField('อายุ',max_length=255)
    
    def __str__(self):
        return self.name
    


class Sale(models.Model):
    name = models.CharField('ชื่อลูกค้า',max_length=255)#ชื่อลูกค้า
    
    web = models.ForeignKey(Web,on_delete=models.CASCADE)#ลูกค้าของเว็บ
    interest = models.ForeignKey(Interest,on_delete=models.CASCADE)#ความสนใจ
    source = models.ForeignKey(Source,on_delete=models.CASCADE)#ที่มาของลูกค้า
    
    choice_buy = models.TextChoices("BUY", "ซื้อ ยังไม่ซื้อ")
    buy = models.CharField('ซื้อ หรือ ไม่ซื้อ ?',default="ยังไม่ซื้อ",blank=True, choices=choice_buy.choices, max_length=50)#ซื้อไม่ซื้อ
    
    MedalType = models.TextChoices("MedalType", "ชาย หญิง")
    sex = models.CharField('เพศ',blank=True, choices=MedalType.choices, max_length=10)#เพศ
    age = models.ForeignKey(Age,on_delete=models.CASCADE)#อายุ
    
    quantity = models.IntegerField(default=1,null=True,blank=True)
    
    choice_unit = models.TextChoices("unit", "บาท ใบ ยูสเซอร์")
    unit = models.CharField('หน่วย',choices=choice_unit.choices,max_length=10,null=True,blank=True)
    
    choice_callback = models.TextChoices("choice_callback", "Line Facebook Tiktok Youtube Website Other")
    call_back = models.CharField('ช่องทางติดต่อกลับ',choices=choice_callback.choices,max_length=100,null=True,blank=True)
    other = models.TextField('หมายเหตุการติดต่อ',null=True,blank=True)#หมายเหตุ
    
    user_account = models.ForeignKey(User,on_delete=models.CASCADE)#ผู้ลงทะเบียน
    create_date = models.DateTimeField(auto_now_add=True) #วันลงทะเบียน
    
    class Meta:
        ordering = ["id"]
        verbose_name_plural = "Sale"
        verbose_name = "name"

    def __str__(self):
        return self.name