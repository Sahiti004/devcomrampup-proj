from django.db import models

class hostelsportsequipment(models.Model):
    equipname=models.CharField(max_length=50)
    borrowstatus=models.CharField(max_length=50)
    
    def __str__(self):
        return self.equipname