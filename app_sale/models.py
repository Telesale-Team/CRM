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
    name = models.CharField('เบอร์โทรศัพท์',max_length=255)#เบอร์โทรศัพท์
    
    web = models.ForeignKey(Web,on_delete=models.CASCADE)#ลูกค้าของเว็บ
    interest = models.ForeignKey(Interest,on_delete=models.CASCADE)#ความสนใจ
    source = models.ForeignKey(Source,on_delete=models.CASCADE)#ที่มาของลูกค้า
    
    #ส่วนของ user password ลูกค้า
    
    user_id_customer = models.CharField('User login',max_length=255,blank=True)#username
    user_password_customer = models.CharField('Password',max_length=255,blank=True)#พาสลูกค้า
    
    #ส่วนของธนาคาร
    
    user_bank_name = models.CharField('ชื่อบัญชี',max_length=255,blank=True) #เลขบัญชีธนาคาร
    user_id_bank = models.CharField('หมายเลขบัญชีธนาคาร',max_length=255,blank=True)#ชื่อลูกค้า
    
    #สถานะการซื้อ
    choice_buy = models.TextChoices("BUY", "ซื้อ ยังไม่ซื้อ")
    buy = models.CharField('สถานะซื้อ',default="ยังไม่ซื้อ",blank=True, choices=choice_buy.choices, max_length=50)#สถานะการซื้อ
    
    #เพศ อายุ
    MedalType = models.TextChoices("MedalType", "ชาย หญิง")
    sex = models.CharField('เพศ',blank=True, choices=MedalType.choices, max_length=10)#เพศ
    age = models.ForeignKey(Age,on_delete=models.CASCADE)#อายุ
    
    #จำนวนการซื้อ
    quantity = models.IntegerField('จำนวนซื้อ',default=1,null=True,blank=True)
    choice_unit = models.TextChoices("unit","บาท")
    unit = models.CharField('หน่วย',default='บาท',choices=choice_unit.choices,max_length=10,null=True,blank=True)
    
    choice_callback = models.TextChoices("choice_callback", "Line Facebook Tiktok Youtube Website Other")
    call_back = models.CharField('ติดต่อลูกค้า',choices=choice_callback.choices,max_length=100,null=True,blank=True)
    other = models.TextField('หมายเหตุ',null=True,blank=True)#หมายเหตุ
    
    user_account = models.ForeignKey(User,on_delete=models.CASCADE,blank=True)
    create_date = models.DateTimeField(auto_now_add=True) #วันลงทะเบียน
    
    facebook = models.CharField('ช่องทางติดต่อ FB',max_length=255,blank=True)
    line = models.CharField('ช่องทางติดต่อ Line',max_length=255,blank=True)
    check = models.BooleanField(default='')

    
    check_user = models.BooleanField(default=True)
    
    class Meta:
        ordering = ["-id"]
        verbose_name_plural = "Sale"
        verbose_name = "name"

    def __str__(self):
        return self.name