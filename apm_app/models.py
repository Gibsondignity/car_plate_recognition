from django.db import models

from account.models import Acount_User


class CarInfo(models.Model):
    car_number = models.CharField(max_length=50)
    owner_name = models.CharField(max_length=50)
    picture = models.FileField(upload_to='media/')
    owner_dob = models.DateField()
    car_model = models.CharField(max_length=50)
    car_type = models.CharField(max_length=50)
    color = models.CharField(max_length=50)
    date_of_reg = models.DateTimeField()
    region_of_reg = models.CharField(max_length=50)
    date_created = models.DateTimeField(auto_now=True)
    date_updated = models.DateTimeField(auto_now_add=True)
    
    
    def __str__(self):
        return self.car_number
    
    
class reportedCar(models.Model):
    car_number = models.ForeignKey(CarInfo, on_delete=models.CASCADE)
    reported_issue = models.CharField(max_length=100, null=True, blank=True)
    reported_by = models.ForeignKey(Acount_User, on_delete=models.CASCADE, null=True, blank=True)
    reported_date = models.DateTimeField(auto_now=True, null=True, blank=True)
    date_updated = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    
    
    def _str__(self):
        return self.car_number

    