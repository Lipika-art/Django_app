from django.db import models

# Create your models here.
class Contact(models.Model):
    name= models.CharField(max_length=122)
    email=models.CharField(max_length=122)
    phone=models.CharField(max_length=12)
    desc=models.TextField()
    date=models.DateField()
    

    # to display users name in the list instead of object(1)

    def __str__(self):
        return self.name
        