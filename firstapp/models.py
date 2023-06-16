from django.db import models


class Person(models.Model):
    name = models.CharField(max_length=20)
    age = models.IntegerField()
    objects = models.Manager()
    DoesNotExist = models.Manager

class Company(models.Model):
    name = models.CharField(max_length=30)


class Product(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    name = models.CharField(max_length=30)
    price = models.IntegerField()

    # создаем объект Company с именем Электрон
firma = Company.objects.create(name=" Электрон")
    # создание товара компании
firma.product_set.create(name="Samsung S20", price=42000)
    # отдельное создание объекта с последующим добавлением в БД
ipad = Product(name="iPad", price=34200) # при добавлении необходимо указать параметр bulk =False
firma.product_set.add(ipad, bulk=False)
    # исключает из компании все товары, # при этом товары остаются в БД и не привязаны к компании # pаботaeт, если в 3ависимой модели ForeignKey(Company, null = True)

    # то же самое, только в отношении одного объекта
ipad = Product.objects.get(name="iPad")
firma.product_set.remove(ipad)