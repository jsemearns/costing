from django.db import models


# Create your models here.
class InventoryItem(models.Model):
    MEASUREMENT_UNITS = [
        ('mL', 'milliliter'),
        ('L', 'liter'),
        ('dL', 'deciliter'),
        ('tsp.', 'teaspoon'),
        ('tbsp.', 'tablespoon'),
        ('fl oz', 'fluid ounce'),
        ('c', 'cup'),
        ('pt', 'pint'),
        ('qt', 'quart'),
        ('gal', 'gallon'),
        ('mg', 'milligram'),
        ('g', 'gram'),
        ('kg', 'kilogram'),
        ('lb', 'pound'),
        ('oz', 'ounce')
    ]
    name = models.CharField(max_length=255)
    unit = models.CharField(max_length=10, choices=MEASUREMENT_UNITS)
    price_per_unit = models.FloatField()
    ap_weight = models.FloatField()
    trim_weight = models.FloatField()

    @property
    def ep_weight(self) -> float:
        return self.ap_weight - self.trim_weight

    @property
    def yield_percentage(self) -> float:
        return (self.ep_weight / self.ap_weight) * 100


class Recipe(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)
    inventory_items = models.ManyToManyField(InventoryItem)