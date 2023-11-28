from django.db import models
from django.contrib.auth.models import User as adminUser

# Create your models here.
class User(models.Model):
    first_name=models.CharField(max_length=30,)
    last_name=models.CharField(max_length=20)
    email=models.EmailField(max_length=30,unique=True)
    def __str__(self):
        return self.first_name
    

class UserProfileInfo(models.Model):
    user=models.OneToOneField(adminUser,on_delete=models.CASCADE)

    #additional
    portfolio=models.URLField(blank=True)
    profile_pic=models.ImageField(upload_to='profile_pics',blank=True)

    def __str__(self):
        return self.user.username
    
