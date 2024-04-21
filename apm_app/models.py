from django.db import models

from account.models import Acount_User
from django.utils import timezone


# class CarOwner(models.Model):
#     owner_name = models.CharField(max_length=50)
#     owner_dob = models.DateField()
#     owner_phone = models.CharField(max_length=50)
#     owner_email = models.EmailField()
#     owner_address = models.CharField(max_length=100)
#     owner_national_id = models.CharField(max_length=50)
#     owner_nationality = models.CharField(max_length=50)
#     picture = models.FileField(upload_to='media/')
    
#     def __str__(self) -> str:
#         return f'{self.owner_phone } - {self.owner_name}'
    
    
class CarInfo(models.Model):
    owner_name = models.CharField(max_length=50, null=True)
    owner_dob = models.DateField(blank=True, null=True)
    owner_phone = models.CharField(max_length=50, null=True)
    owner_email = models.EmailField(null=True)
    owner_address = models.CharField(max_length=100, null=True)
    owner_national_id = models.CharField(max_length=50, null=True)
    owner_nationality = models.CharField(max_length=50, null=True)
    picture = models.FileField(upload_to='media/', null=True, blank=True)
    
    car_number = models.CharField(max_length=50, null=True)
    car_model = models.CharField(max_length=50, null=True)
    car_type = models.CharField(max_length=50, null=True)
    color = models.CharField(max_length=50, null=True)
    date_of_reg = models.DateTimeField(default=timezone.now())
    region_of_reg = models.CharField(max_length=50)
    date_created = models.DateTimeField(auto_now=True)
    date_updated = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name_plural = "Car Information"
        
    def __str__(self):
        return self.car_number
    
    
class reportedCar(models.Model):
    car_number = models.ForeignKey(CarInfo, on_delete=models.CASCADE)
    reported_issue = models.CharField(max_length=100, null=True, blank=True)
    reported_by = models.ForeignKey(Acount_User, on_delete=models.CASCADE, null=True, blank=True)
    reported_date = models.DateTimeField(auto_now=True, null=True, blank=True)
    date_updated = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    
    class Meta:
        verbose_name_plural = "Reported Cars"
        
        
    def __str__(self):
        return self.car_number
    
    
    
class EntryCars(models.Model):
    car_number = models.ForeignKey(CarInfo, on_delete=models.CASCADE)
    entry_date = models.DateTimeField(auto_now=True)
    entry_time = models.DateTimeField(auto_now=True)
    entry_by = models.ForeignKey(Acount_User, on_delete=models.CASCADE, null=True, blank=True)
    entry_reason = models.CharField(max_length=100)
    entry_status = models.BooleanField(default=False)
    date_updated = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    
    
    class Meta:
        verbose_name_plural = "Entery Cars"
    
    def __str__(self):
        return f"{self.car_number} {self.entry_date}" 
    


    