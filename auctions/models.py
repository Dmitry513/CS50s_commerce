from django.contrib.auth.models import AbstractUser
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models


class User(AbstractUser):
    gender = models.TextField(max_length=1, blank=True, null=True)


class Commodity(models.Model):
    name = models.TextField(max_length=32)
    description = models.TextField(max_length=600)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='commodities')
    image = models.ImageField(upload_to='images/', null=True, blank=True)
    startprice = models.PositiveIntegerField(default=0, validators=[MaxValueValidator(1e8)])

    def __str__(self):
        return f'{self.name}'


class Bid(models.Model):
    user = models.ForeignKey(User, on_delete=models.PROTECT, related_name='bids')
    commodity = models.ForeignKey(Commodity, on_delete=models.CASCADE)
    bid_time = models.DateTimeField(auto_now=True)
    value = models.PositiveIntegerField(default=1, validators=[MinValueValidator(1)])

    def __str__(self):
        return f'{self.user.username}: {self.value}'


class Comment(models.Model):
    comment = models.TextField(max_length=320)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True, related_name='comments')
    commodity = models.ForeignKey(Commodity, on_delete=models.CASCADE, related_name='comments')
    published_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.user.username}: {self.comment[:15]}'
