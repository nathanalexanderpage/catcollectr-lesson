from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Cat:
    def __init__(self, name, breed, description, age):
        self.name = name
        self.breed = breed
        self.description = description
        self.age = age
        user = models.ForeignKey(User, on_delete=models.CASCADE)
        likes = models.IntegerField(default=0)
    def __str__(self):
	  return self.name
