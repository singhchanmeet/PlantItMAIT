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
    plant_id=models.CharField(max_length=3,default='')
    plant_name=models.CharField(max_length=1000,default='')
    scientific_name=models.CharField(max_length=1000,default='')
    plant_descriptionp=models.CharField(max_length=1000,default='')
    plant_pic=models.ImageField(upload_to='media/')   #upload_to='/static/media'
    season=models.CharField(max_length=200,default='')
    soil=models.CharField(max_length=100,default='')
    location=models.CharField(max_length=100,default='')
    cost=models.CharField(max_length=100,default='')
    size=models.CharField(max_length=100,default='')
    sunlight=models.CharField(max_length=100,default='')
    medicinal_use=models.CharField(max_length=100,default='')
    plant_type=models.CharField(max_length=100,default='')

    def __str__(self):
        return self.plant_name
    