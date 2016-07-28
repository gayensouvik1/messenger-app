from django.db import models
from django.contrib.auth.models import User



class Document(models.Model):
    docfile = models.FileField(upload_to='documents/%Y/%m/%d')

class Message(models.Model):
	receiver = models.CharField(max_length = 200)
	sender = models.CharField(max_length = 200)
	message = models.CharField(max_length = 1000)

	def __str__(self):
		return self.message



