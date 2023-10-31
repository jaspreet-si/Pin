from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Pin(models.Model):
    Pin_by=models.ForeignKey(User,on_delete=models.CASCADE)
    Pin_name=models.CharField(max_length=200)
    Pin_img=models.ImageField(upload_to='pinss')
    Pin_discription=models.TextField()
    Pin_time=models.DateTimeField(auto_now_add=True)
    Likes=models.ManyToManyField(User,blank=True,null=True,related_name='likes')

    def __str__(self):
        return self.Pin_name

    def number_of_likes(self):
        return self.Likes.count()

class Comments(models.Model):
    Comment_by=models.ForeignKey(User,on_delete=models.CASCADE)
    Comment_on=models.ForeignKey(Pin,on_delete=models.CASCADE)
    Comment=models.TextField(blank=True,null=True)
    Comment_timming=models.DateTimeField(auto_now_add=True)
    
class profile(models.Model): 
    username=models.OneToOneField(User,on_delete=models.CASCADE)
    profile_picture=models.ImageField(upload_to='profile_photos')

    
