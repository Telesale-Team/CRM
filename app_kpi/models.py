from django.db import models

from app_user.models import *
from app_money.models import *
from django.utils import timezone

class Create_Interrest(models.Model):
    name = models.CharField("ประเภทลูกค้า", max_length=50)
    
    def __str__(self):
        return str(self.name)


class Kpi (models.Model):

    team = models.ForeignKey(Team,on_delete=models.CASCADE)
    name = models.ForeignKey(ProfileUser,on_delete=models.CASCADE)
    new_customer = models.IntegerField(default=0)   #ลูกค้าใหม่
    slakthai = models.IntegerField(default=0) # สลากไท
    mughuay = models.IntegerField(default=0) # มักหวย
    member = models.IntegerField(default=0)  #`จำนวนสมาชิก`
    pay = models.IntegerField(default=0)     #`รายจ่าย`
    income = models.IntegerField(default=0) #รายได้
    profit = models.IntegerField(default=0) #`กำไร`
    created = models.DateTimeField(default=timezone.now) #วันที่

    def __str__(self):
        return str(self.created)
    
class Dashboard (models.Model):
    
    team = models.ForeignKey(Team,on_delete=models.CASCADE)
    duckbet = models.PositiveIntegerField()
    rx7 = models.PositiveIntegerField()
    thaiban = models.PositiveIntegerField()
    
    def __str__(self):
        return str(self.team)
    
    
class Customer_Interest (models.Model):
    user_buy = models.BooleanField('สมัครซื้อแล้ว',default=False)
    username = models.ForeignKey(User,on_delete=models.CASCADE)
    user_customer = models.CharField('username ลูกค้า ',max_length=20)
    user_type = models.ForeignKey(Create_Interrest,on_delete=models.CASCADE,null=True,blank=True)
    user_telephone = models.CharField('เบอร์โทรลูกค้า ',max_length=10)
    user_qutity = models.PositiveIntegerField('จำนวนการซื้อ')
    MedalType = models.TextChoices("MedalType", "บาท ใบ ครั้ง")
    unit = models.CharField(blank=True, choices=MedalType.choices, max_length=10)
    page_name = models.CharField('ที่มาลูกค้า',max_length=255)
    detail = models.CharField('รายละเอียดเพิ่มเติม',max_length=255)
    
    
    
    def __str__(self):
        return str(self.username)
    
    
