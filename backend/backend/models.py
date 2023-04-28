from django.db import models

class User(models.Model):
    user_id = models.IntegerField(primary_key=True)
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)

class Arrival(models.Model):
    arrival_id = models.IntegerField(primary_key=True)
    arrival_time = models.DateTimeField()
    