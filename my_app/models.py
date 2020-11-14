from django.db import models

# Create your models here.
class Friends(models.Model):
    name=models.CharField(max_length=250)
    age = models.IntegerField()
    address=models.CharField(max_length=250)

    def __str__(self):
        return self.name
class Category(models.Model):
    name=models.CharField(max_length=250)
    def __str__(self):
        return self.name

class Products(models.Model):
    name=models.CharField(max_length=250)
    price=models.IntegerField()
    description=models.TextField(blank=True,null=True)
    Category=models.ForeignKey(Category, on_delete = models.CASCADE,blank=True,null=True)
    discount=models.IntegerField(default=0)
    def __str__(self):
        return self.name