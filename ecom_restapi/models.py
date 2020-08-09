from django.db import models

# Create your models here.
class Categories(models.Model):
    product_category = models.CharField(max_length=50, primary_key=True)

    def __str__(self):
        return '{}'.format(self.product_category)

class SubCategories(models.Model):
    product_category = models.ForeignKey(Categories,on_delete=models.CASCADE)
    product_subcategory = models.CharField(max_length=50, primary_key=True)

    def __str__(self):
        return '{} {}'.format(self.product_category, self.product_subcategory)

class Products(models.Model):
    product_id = models.BigIntegerField(primary_key=True)
    product_title = models.CharField(max_length=85)
    product_category = models.ForeignKey(Categories,on_delete=models.CASCADE)
    product_subcategory = models.ForeignKey(SubCategories,on_delete=models.CASCADE)
    unitprice = models.FloatField()
    quantity = models.IntegerField()
    totalprice = models.FloatField()

    def __str__(self):
        return '{} {} {}'.format(self.product_category, self.product_subcategory, self.product_title)