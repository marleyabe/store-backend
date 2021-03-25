from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField('Name', max_length=25, null=True)

    def __str__(self):
        return '{}'.format(self.name)

    def __repr__(self):
        return '<Product name={}>'.format(self.name)


class Category(models.Model):
    name = models.CharField('Name', max_length=25, null=True)
    product = models.ForeignKey(Product, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return '{}'.format(self.name)

    def __repr__(self):
        return '<Category name={}>'.format(self.name)


class SubCategory(models.Model):
    name = models.CharField('Name', max_length=25, null=True)
    category = models.ForeignKey(Category, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return '{}'.format(self.name)

    def __repr__(self):
        return '<SubCategory name={}>'.format(self.name)


class Item(models.Model):
    name = models.CharField('Name', max_length=25, null=True)
    description = models.TextField('Description', null=True)
    price = models.CharField('Price', max_length=10, null=True)
    subCategory = models.ManyToManyField(SubCategory, null=True)

    def __str__(self):
        return '{}'.format(self.name)

    def __repr__(self):
        return '<Item name={}>'.format(self.name)
