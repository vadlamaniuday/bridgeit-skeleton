from django.db import models


# Create your models here.
class Mobiles(models.Model):
    company = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    processor = models.CharField(max_length=100)
    camera = models.CharField(max_length=100)  # You can use a more specific field type if needed
    ram = models.IntegerField()  # Assuming RAM is in GB
    rom = models.IntegerField()  # Assuming ROM is in GB
    price = models.DecimalField(max_digits=10, decimal_places=2)  # Assuming price is in a currency format
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.company} {self.model}"
