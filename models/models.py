from django.db import models


# Main models
class Product(models.Model):
    category = models.CharField(max_length=150)
    title = models.CharField(max_length=150)
    link = models.URLField(max_length=150, unique=True)
    shop = models.CharField(max_length=150)

    def __str__(self):
        return self.category + ' ' + self.title + ' from ' + self.shop


class History(models.Model):
    price = models.IntegerField(default=None)
    date = models.DateTimeField(auto_now_add=True)
    product_id = models.ForeignKey(Product, related_name='prices', on_delete=models.CASCADE, default=None)

    def __str__(self):
        return 'At ' + self.date.strftime("%m/%d/%Y, %H:%M:%S") + " price was " + str(self.price)

# Parser models
