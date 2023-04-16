from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Subject (models.Model):
    name = models.CharField(max_length=255)
    def __str__(self) :
        return self.name
    
class ReceiptInvoice (models.Model): # การเบิกเงิน
    collector = models.OneToOneField(User,on_delete=models.CASCADE)#ผู้เบิก
    subject = models.OneToOneField(Subject,on_delete=models.CASCADE) # เรื่องขอเบิก
    details = models.TextField(null=True,blank=True) #รายละเอียดการเบิก
    money = models.PositiveBigIntegerField(default=0,blank=True) #จำนวนเงิน
    image1 = models.ImageField(upload_to='image_money',null=True,blank=True,default='default.png') #ภาพขอเบิกเงินที่ 1
    image2 = models.ImageField(upload_to='image_money',null=True,blank=True,default='default.png') #ภาพขอเบิกเงินที่ 2
    image3 = models.ImageField(upload_to='image_money',null=True,blank=True,default='default.png') #ภาพขอเบิกเงินที่ 3
    image4 = models.ImageField(upload_to='image_money',null=True,blank=True,default='default.png') #ภาพขอเบิกเงินที่ 4
    image5 = models.ImageField(upload_to='image_money',null=True,blank=True,default='default.png') #ภาพขอเบิกเงินที่ 5

    created_dat = models.DateField(auto_now_add=True,null=True,blank=True) #วันที่เบิก
    
    
    def __str__(self):
        return str(self.collector)
    
    
class Sorary (models.Model): # เงินเดือน

    money = models.IntegerField(default=0) #เงินเดือน
    outmoney = models.PositiveIntegerField(default=0)
    
    
    
    def __str__(self):
        return str(self.outmoney)+' '+ str(self.money)
    
