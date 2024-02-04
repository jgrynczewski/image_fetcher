from django.db import models
from django.contrib.auth import get_user_model


User = get_user_model()


class Image(models.Model):
    url = models.URLField()
    image = models.ImageField(upload_to='media/')
    name = models.CharField(max_length=100)
    owner = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    send_to = models.ManyToManyField('Receiver', through='ImageReceiver')
    created_at = models.DateTimeField(auto_now_add=True)


class Receiver(models.Model):
    name = models.CharField(max_length=200)
    address = models.CharField(max_length=200, null=True)
    created_at = models.DateTimeField(auto_now_add=True)


class ImageReceiver(models.Model):
    image = models.ForeignKey(Image, on_delete=models.CASCADE)
    receiver = models.ForeignKey(Receiver, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
