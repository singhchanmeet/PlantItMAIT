from django.db import models

# Create your models here.
class Contact(models.Model):
    name=models.CharField(max_length=40)
    email=models.CharField(max_length=50)
    phone=models.CharField(max_length=13)
    message=models.TextField()
    def __str__(self):
        return self.name
    
class Plant(models.Model) :
    plant_id=models.CharField(max_length=2,default='')
    plant_name=models.CharField(max_length=40)
    plant_pic=models.ImageField(upload_to='media/')   #upload_to='/static/media'
    season=models.CharField(max_length=200)
    soil=models.CharField(max_length=100)
    location=models.CharField(max_length=100)
    cost=models.CharField(max_length=100)
    def __str__(self):
        return self.plant_name
    