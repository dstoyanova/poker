from django.db import models
from django.contrib.auth.models import User


class Session(models.Model):
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    name = models.CharField(max_length=128)
    description = models.TextField(max_length=516, blank=True, null=True)
    CARDS_CHOICES = [
        ('1', '1,2,3,5,8,13,20,40,100'),
        ('2', '1,2,3,5,8,13,20,40,?'),
        ('3', '0,1,2,4,8,16,32,64'),
        ('4', '1,2,4,8,12,16,24,40,80'),
        ('5', '☕,1,2,3,5,8,13,20,?'),
        ('6', 'XS,S,M,L,XL,XXL,?'),
        ('7', '1,2,5,10,20,50,100'),
        ('8', '1,2,3,4,5'),
    ]
    cards = models.CharField(max_length=1, choices=CARDS_CHOICES, default='1')
    ACCESS_CHOICES = [
        ('PU', 'Public'),
        ('PR', 'Private')
    ]
    access = models.CharField(max_length=2, choices=ACCESS_CHOICES, default='PU')
    access_code = models.CharField(max_length=5, blank=True, null=True)


class Vote(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    session = models.ForeignKey('Session', on_delete=models.CASCADE)
    vote_value = models.CharField(max_length=3)
