from django.db import models
from rest_framework import serializers

# from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.db.models import (
    CASCADE,
    CharField,
    DateTimeField,
    ForeignKey,
    ManyToManyField,
    Model,
    TextField,
)


class Message(models.Model):
    subject = models.CharField(max_length=200)
    body = models.TextField()


class MessageSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Message
        fields = ('url', 'subject', 'body', 'pk')


class User(AbstractUser):
    followers = ManyToManyField('self', related_name='followees', symmetrical=False)


class Post(Model):
    author = ForeignKey(User, related_name='posts', on_delete=CASCADE)

    created = DateTimeField(auto_now_add=True)
    content = TextField(blank=True, null=True)
    title = CharField(max_length=255)
    updated = DateTimeField(auto_now=True)
