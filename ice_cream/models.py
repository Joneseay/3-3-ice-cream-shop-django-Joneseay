from django.db import models

class IceCream(models.Model):
    available_choices = [('DAILY', 'daily'), ('WEEKLY', 'weekly'), ('SEASONAL', 'seasonal')]
    base_choices = [('CHOCOLATE','chocolate'),('VANILLA', 'vanilla')]
    flavor = models.CharField(max_length= 100)
    base = models.CharField(max_length= 100, choices=base_choices)
    available = models.CharField(max_length= 100, choices=available_choices)
    featured = models.BooleanField()
    date = models.DateField()

    def __str__(self):
        return self.flavor
# Create your models here.