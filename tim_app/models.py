from django.db import models
from django.utils import timezone
from django.core.validators import MaxValueValidator


class User(models.Model):
	username = models.CharField(max_length = 32, primary_key = True)
	password = models.CharField(max_length = 32)
	phoneNr = models.CharField(max_length = 32)
	email = models.EmailField(blank = True)
	location = models.CharField(max_length = 32)
	radius = models.IntegerField(default = 0)

	def __str__(self):
		return self.username


class Request(models.Model):
	id = models.AutoField(primary_key = True)
	username = models.ForeignKey('User')
	goodName = models.ForeignKey('Good')
	active = models.BooleanField(default = True)
	misc = models.CharField(max_length = 256, blank = True)
	quantity = models.PositiveSmallIntegerField()
	priority = models.PositiveSmallIntegerField(validators=[MaxValueValidator(3)])
	location = models.CharField(max_length = 32)
	radius = models.IntegerField(default = 0)
	creationDate = models.DateTimeField(default = timezone.now)

	def create(self):
		self.creationDate = timezone.now()
		self.save()

	def __str__(self):
		return (str)(self.id) + ':' + (str)(self.username) + ',' + (str)(self.goodName)


class Supply(models.Model):
	id = models.AutoField(primary_key = True)
	username = models.ForeignKey('User')
	goodName = models.ForeignKey('Good')
	active = models.BooleanField(default = True)
	misc = models.CharField(max_length = 256, blank = True)
	quantity = models.PositiveSmallIntegerField()
	location = models.CharField(max_length = 32)
	radius = models.IntegerField(default = 0)
	creationDate = models.DateTimeField(default = timezone.now)

	def create(self):
		self.creationDate = timezone.now()
		self.save()

	def __unicode__(self):
		return self.id

	def __str__(self):
		return (str)(self.id) + ':' + (str)(self.username) + ',' + (str)(self.goodName)

class Good(models.Model):
	goodName = models.CharField(max_length = 64, primary_key = True)
	unit = models.CharField(max_length = 16)
	description = models.CharField(max_length = 256)

	def __str__(self):
		return self.goodName

