from django.db import models
from django.contrib.auth.models import User




# Create your models here.

class Positions (models.Model):
    name = models.CharField('ตำแหน่งงาน',max_length=255,unique=True)
    class Meta:
        ordering = ["-id"]
        verbose_name_plural = "Create Position"
        verbose_name = "Name Position"
    
    def __str__(self):
        return self.name

class Skill (models.Model):
    name = models.CharField('สกิลการทำงาน',max_length=255,unique=True)
    
    class Meta:
        ordering = ["-id"]
        verbose_name_plural = "Create Skill"
        verbose_name = "Name Skill"
    
    def __str__(self):
        return self.name
    
class Team (models.Model):
    name = models.CharField('ชื่อทีม',max_length=255)
    image =  models.ImageField('สัญญาลักษณ์ทีม',upload_to='image_teams',null=True,blank=True,default='default.png') #รูปถ่าย
    detail = models.CharField('รายละเอียดเพิ่มเติม',max_length=255,null=True,blank=True)
    
    class Meta:
        ordering = ["-id"]
        verbose_name_plural = "Create Team"
        verbose_name = "Name Team"
    
    def __str__(self):
        return self.name


class ProfileUser(models.Model):
    
    username = models.OneToOneField(User,on_delete=models.CASCADE) # ชื่อพนักงาน
    image_profile = models.ImageField('รูปภาพโปรไฟล์',upload_to='image_profile',null=True,blank=True,default='default.png')#รูปภาพโปรไฟล์
    
    nickname = models.CharField('ชื่อพนักงาน',max_length=20,blank=True)	# ชื่อเล่นพนักงาน
    address = models.CharField('ที่อยู่',max_length=255,blank=True,null=True)# ที่อยู่ 
    phone = models.CharField('เบอร์โทรศัพท์',max_length=10,blank=True) #  เบอร์โทรศัพท์
    image_id_card = models.ImageField('สำเนาบัตรประชาชน',upload_to='image_id_card',null=True,blank=True,default='default.png')#สำเนาบัตรประชาชน
    
    bank_id = models.IntegerField('หมายเลขบัญชีธนาคาร',blank=True,null=True)#หมายเลขบัญชีธนาคาร
    image_bank = models.ImageField('สำเนาบัญชีธนาคาร',upload_to='image_bank',null=True,blank=True,default='default.png') #สำเนาบัญชีธนาคาร
    
    level = models.TextChoices("Level", "ฝ่ายการตลาด ฝ่ายสต๊อกสินค้า ฝ่ายการเงินการบัญชี ฝ่ายบุคคล")
    permission = models.CharField('สิทธิ์การใช้งาน',blank=True, choices=level.choices, max_length=21)#สิทธิ์การใช้งาน
    
    team = models.ForeignKey(Team,on_delete=models.CASCADE,blank=True,null=True)#ฝาย
    position = models.ForeignKey(Positions,on_delete=models.CASCADE,blank=True,null=True)#ตำแหน่งงาน

    
    MedalType = models.TextChoices("MedalType", "น้อยกว่า1ปี 1ปี 2ปี มากกว่า3ปี")
    working_experience = models.CharField('ประสบการณ์ทำงาน',blank=True, choices=MedalType.choices, max_length=20)#ประสบการณ์ทำงาน
    
    working_skill = models.ForeignKey(Skill,on_delete=models.CASCADE,blank=True,null=True)#ทักษะการทำงาน
    worked_date = models.DateTimeField('วันเริ่มงาน',auto_now_add=True,blank=True,null=True)#วันเริ่มงาน
    
    
    
    image_check = models.BooleanField(default=False)
    other = models.TextField('หมายเหตุ',max_length=255,blank=True)

    
    
    class Meta:
        ordering = ["-username"]
        verbose_name_plural = "Profile"
        verbose_name = "Member"

    def __str__ (self):
        return str(self.username)
    

