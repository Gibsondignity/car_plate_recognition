from django.db import models
from django.contrib.auth.models import User, Group
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser, PermissionsMixin
from django.core.exceptions import ValidationError
# Create your models here.

def validate_image(image):
    file_size = image.file.size
    limit_kb = 150
    if file_size > limit_kb * 1024:
        raise ValidationError("Max size of file is %s KB" % limit_kb)



class SecurityQuestion(models.Model):
    question_text = models.CharField(max_length=200)
    
    def __str__(self):
        return self.question_text
    
    
    
class Acount_User(AbstractUser):

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    first_name = models.CharField(max_length=200, null=True, blank=True)
    second_name = models.CharField(max_length=200, null=True, blank=True)
    phone = models.CharField(max_length=200 , blank=True ,null=True, unique=True)
    #profile = models.FileField(upload_to="profile/", null=True, blank=True, validators=[validate_image])
    
    
    def __str__(self):
        return self.username
    
    

class SecurityAnswer(models.Model):
    user = models.OneToOneField(Acount_User, on_delete=models.CASCADE)
    question = models.ForeignKey(SecurityQuestion, on_delete=models.CASCADE)
    answer_text = models.CharField(max_length=200)
    
    def __str__(self):
        return self.answer_text
    

    
    
    