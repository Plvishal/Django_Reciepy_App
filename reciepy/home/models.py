from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Reciepy(models.Model):
    user=models.ForeignKey(User,on_delete=models.SET_NULL,null=True,blank=True)
    receipy_name=models.CharField(max_length=100)
    receipy_des=models.TextField()
    receipy_img=models.ImageField(upload_to="receipeimage")
