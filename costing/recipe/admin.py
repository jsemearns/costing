from django.contrib import admin
from recipe.models import InventoryItem, Recipe

# Register your models here.
admin.site.register(InventoryItem)
admin.site.register(Recipe)