import uuid

from django.db import models
from datetime import datetime


# Create your models here.

class Data(models.Model):
    title = models.CharField(max_length=150)
    link = models.URLField(max_length=150)
    price = models.IntegerField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Category(models.Model):
    title = models.CharField(max_length=150)
    link = models.URLField(max_length=150, unique=True)
    shop = models.CharField(max_length=150)


class ProductHistory(models.Model):
    price = models.IntegerField(default=None)
    date = models.DateTimeField(auto_now_add=True)

    def __init__(self, Category1):
        category_id = models.ForeignKey(Category1, on_delete=models.CASCADE, default=None)

class Phone(Category):

    def __str__(self):
        return 'PHONE ' + self.title + ' from ' + self.shop


class Laptop(Category):

    def __str__(self):
        return 'LAPTOP ' + self.title + ' from ' + self.shop


class Keyboard(Category):

    def __str__(self):
        return 'KEYBOARD ' + self.title + ' from ' + self.shop


class Monitor(Category):

    def __str__(self):
        return 'MONITOR ' + self.title + ' from ' + self.shop


class PhoneHistory(ProductHistory):
    def __str__(self):
        return 'PHONE_HISTORY ' + str(self.price) + ' ' + self.date.strftime(
            "%m/%d/%Y, %H:%M:%S")


class LaptopHistory(ProductHistory):
    def __str__(self):
        return 'LAPTOP_HISTORY ' + str(self.price) + ' ' + self.date.strftime(
            "%m/%d/%Y, %H:%M:%S")


class KeyboardHistory(ProductHistory):
    def __str__(self):
        return 'KEYBOARD_HISTORY ' + str(self.price) + ' ' + self.date.strftime(
            "%m/%d/%Y, %H:%M:%S")


class MonitorHistory(ProductHistory):
    def __str__(self):
        return 'MONITOR_HISTORY ' + str(self.price) + ' ' + self.date.strftime(
            "%m/%d/%Y, %H:%M:%S")
