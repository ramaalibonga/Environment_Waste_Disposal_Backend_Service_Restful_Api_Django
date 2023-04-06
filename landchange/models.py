from django.db import models


class Address(models.Model):
      region_list = [("Dar","Dar es salaam"),]
      dictrict_list = [("Ilala","Ilala")]
      regional_name = models.CharField(max_length=255,choices=region_list)
      dictrict_name = models.CharField(max_length=255,choices=dictrict_list)


class Landchange(models.Model):
      remark_list = [("Solved","Solved"),("Not Solved","Not Solved")]
      latitude = models.DecimalField(decimal_places=5,max_digits=8)
      longitude = models.DecimalField(decimal_places=5,max_digits=8)
      photo = models.CharField(max_length=255)
      comment_body = models.TextField()
      remark = models.CharField(max_length=255,choices=remark_list)
      address_landchange = models.ForeignKey(Address,on_delete=models.CASCADE,blank=False)


class Admin(models.Model):
     first_name = models.CharField(max_length=255)
     last_name = models.CharField(max_length=255)
     organization = models.CharField(max_length=255)
     position = models.CharField(max_length=255)
     phone = models.CharField(max_length=255)
     email = models.CharField(max_length=255)
     address_admin = models.ForeignKey(Address,on_delete=models.CASCADE,blank=False)

class Comment(models.Model):
      landchange_id = models.ForeignKey(Landchange,on_delete=models.CASCADE,blank=True)
      admin_id = models.ForeignKey(Admin,on_delete=models.CASCADE,blank=True)
      comment_body = models.TextField()
      
