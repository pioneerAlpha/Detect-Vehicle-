from django.db import models
from django.conf import settings
from django.shortcuts import reverse
from django.contrib.auth.models import User

class Index(models.Model):
	image = models.ImageField()