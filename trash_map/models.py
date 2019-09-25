from django.db import models

statuses = [("Принято на рассмотрение", "Принято на рассмотрение"),
            ("Рассмотрено", "Рассмотрено")]


# Create your models here.
class Dump(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    long = models.FloatField(default=0, blank=True)  # долгота
    lat = models.FloatField(default=0, blank=True)  # широта
    street = models.CharField(max_length=100)
    description = models.TextField()
    photo = models.ImageField(upload_to='images/')
    sending_time = models.DateTimeField(auto_now_add=True)
    status = models.CharField(default="Принято на рассмотрение", choices=statuses, max_length=50)
    rating = models.IntegerField(default=0)


class Event(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    long = models.FloatField(default=0, blank=True)
    lat = models.FloatField(default=0, blank=True)
    street = models.CharField(max_length=100)
    org_email = models.EmailField()
    org_phone = models.CharField(max_length=20)
    description = models.TextField()
    rating = models.IntegerField(default=0, blank=True)
