from django.db import models
import random

# Create your models here.


def gen_unique_id(cal):
	res = ''
	for i in range(cal):
		rand = random.choice("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ")
		res = res+rand
	return res


class Product(models.Model):
	title = models.CharField(max_length = 100, verbose_name = 'Название товара')
	description = models.TextField(max_length = 150, verbose_name = 'Описание товара')
	icon  = models.ImageField(upload_to='icon', verbose_name = 'Иконка товара')
	price = models.FloatField(verbose_name = 'Цена товара')
	count = models.IntegerField(default = 0, verbose_name = 'В наличии')
	unique_id = models.CharField(max_length=40, default = gen_unique_id(40))
	
	def __str__(self):
		return self.title
	
	class Meta:
		verbose_name = 'Товар'
		verbose_name_plural = 'Товары'
		ordering = ['-id']


class List(models.Model):
	product_id = models.IntegerField()
	product = models.CharField(max_length = 255)
	

class Setting(models.Model):
	sitename = models.CharField(max_length = 30, verbose_name = 'Название сайта')
	description = models.TextField(max_length = 200, verbose_name = 'Описание сайта')
	footer = models.CharField(max_length = 255, verbose_name = 'Футр')
	token = models.CharField(max_length = 255, verbose_name = 'Qiwi token')
	phone = models.CharField(max_length = 11, verbose_name = 'Номер Qiwi')

	def __str__(self):
		return 'Настройки'

	class Meta:
		verbose_name = 'Настройки'
		verbose_name_plural = 'Настройки'