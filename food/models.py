from django.db import models

# Create your models here.
class Item(models.Model):
    item_name = models.CharField(max_length=200)
    item_desc = models.CharField(max_length=200)
    item_price = models.IntegerField()
    item_image = models.CharField(max_length=500, default="https://static.vecteezy.com/system/resources/previews/010/826/341/original/vacation-icon-isolated-on-transparent-background.png")

    def __str__(self):
        return self.item_name
