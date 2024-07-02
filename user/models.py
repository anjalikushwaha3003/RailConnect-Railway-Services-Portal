from django.utils.crypto import get_random_string

from django.db import models

# Create your models here.
class register(models.Model):
    name=models.CharField(max_length=150,null=True)
    email=models.CharField(max_length=100 , primary_key=True)
    mobile=models.CharField(max_length=20,null=True)
    password=models.CharField(max_length=100,null=True)
    profile=models.ImageField(upload_to='static/images/userpic/' ,null=True)
    address=models.TextField()
    

class contactus(models.Model):
    Query=models.CharField(max_length=100,null=True)
    Name=models.CharField(max_length=200,null=True)
    Email=models.CharField(max_length=100,null=True)
    Mobile=models.CharField(max_length=25,null=True)
    Message=models.TextField(null=True)

class RailwayStation(models.Model):
    name = models.CharField(max_length=255)
    code = models.CharField(max_length=10)

    def __str__(self):
        return f"{self.name} ({self.code})"

    
class feedback(models.Model):
    Rating =models.CharField(max_length=100,null=True)
    Name = models.CharField(max_length=100)
    Email = models.EmailField()
    Mobile = models.CharField(max_length=20)
    Message = models.TextField()

    def __str__(self):
        return f"{self.Name}'s Feedback"

class Booking(models.Model):
    
    train_number = models.CharField(max_length=50)
    class_type = models.CharField(max_length=50)
    station_from = models.CharField(max_length=50)
    station_to = models.CharField(max_length=50)
    name = models.CharField(max_length=100)
    date=models.DateField()
    age = models.IntegerField()
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    )
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    pnr = models.PositiveIntegerField(primary_key=True, unique=True)

    def save(self, *args, **kwargs):
        if not self.pnr:
            self.pnr = self.generate_unique_pnr()
        super().save(*args, **kwargs)

    def generate_unique_pnr(self):
        last_pnr = Booking.objects.order_by('-pnr').first()
        if last_pnr:
            return last_pnr.pnr + 1
        else:
            return 100000