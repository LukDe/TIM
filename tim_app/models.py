from django.db import models
from django.utils import timezone
from django.core.validators import MaxValueValidator


# Create your models here.

class User(models.Model):
	username = models.CharField(max_length = 32, primary_key = True)
	password = models.CharField(max_length = 32)
	mobile = models.CharField(max_length = 32)
	email = models.EmailField(blank = True)
	postalCode = models.CharField(max_length = 32)

	def __str__(self):
		return self.username

class Request(models.Model):
	id = models.AutoField(primary_key = True)
	username = models.ForeignKey('User')
	categoryName = models.ForeignKey('GoodCategory')
	goodName = models.ForeignKey('Good')
	misc = models.CharField(max_length = 256, blank = True)
	quantity = models.PositiveSmallIntegerField()
	priority = models.PositiveSmallIntegerField(validators=[MaxValueValidator(3)])
	catastrophy = models.CharField(max_length = 128)
	creationDate = models.DateTimeField(default = timezone.now)

	def create(self):
		self.creationDate = timezone.now()
		self.save()

	def __unicode__(self):
		return self.id


class Supply(models.Model):
	id = models.AutoField(primary_key = True)
	username = models.ForeignKey('User')
	categoryName = models.ForeignKey('GoodCategory')
	goodName = models.ForeignKey('Good')
	misc = models.CharField(max_length = 256, blank = True)
	quantity = models.PositiveSmallIntegerField()
	creationDate = models.DateTimeField(default = timezone.now)

	def create(self):
		self.creationDate = timezone.now()
		self.save()
	
	def __unicode__(self):
		return self.id

class GoodCategory(models.Model):
	categoryName = models.CharField(max_length = 64, primary_key = True)
	categoryIcon = models.ImageField()

	def __str__(self):
		return self.categoryName

class Good(models.Model):
	goodName = models.CharField(max_length = 64, primary_key = True)
	categoryName = models.ForeignKey(GoodCategory)
	unit = models.CharField(max_length = 16)
	description = models.CharField(max_length = 256)

	def __str__(self):
		return self.goodName



