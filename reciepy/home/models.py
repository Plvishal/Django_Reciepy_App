from django.db import models

# Create your models here.

class Reciepy(models.Model):
    receipy_name=models.CharField(max_length=100)
    receipy_des=models.TextField()
    receipy_img=models.ImageField(upload_to="receipeimage")
