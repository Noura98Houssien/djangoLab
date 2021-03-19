from django.db import models
from products.models.depart import Department
class Item(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    # photo = models.ImageField()
	# image = models.ImageField(null=True, blank=True, upload_to='items/') 
    image=models.ImageField(null=True,blank=True,upload_to='itemss/')
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    # visible = models.BooleanField(default=False)
    active = models.BooleanField(default=False)

    def __str__(self):
       return self.name