from django.db import models

# Create your models here.
class Feedback(models.Model):
    name = models.CharField(max_length=122)
    email = models.CharField(max_length=122)
    rate = models.IntegerField()
    content = models.TextField()
    date = models.DateField()
    
    def __str__(self):
        return self.name
    
class Book(models.Model):
    name = models.CharField(max_length=122)
    phone = models.IntegerField()
    car = models.CharField(max_length=122)
    date = models.IntegerField()
    month = models.CharField(max_length=122)
    year = models.IntegerField()
    fromm = models.CharField(max_length=122)
    to = models.CharField(max_length=122)
    logged_date = models.DateField()

    def __str__(self):
        return self.name
    
    