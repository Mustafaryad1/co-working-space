from django.db import models

# Create your models here.


class Space(models.Model):
    name = models.CharField(max_length=200)
    location = models.CharField(max_length=200)
    contacts = models.CharField(max_length=200)
    owner = models.ForeignKey('auth.User', related_name='spaces', on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Event(models.Model):
    name = models.CharField(max_length=200)
    date = models.DateTimeField()
    number_of_people = models.IntegerField()
    space = models.ForeignKey(Space, related_name='events', on_delete=models.CASCADE)


class Room(models.Model):
    number = models.IntegerField()
    photo = models.FileField(upload_to='room/photos/')
    space = models.ForeignKey(Space, related_name='rooms', on_delete=models.CASCADE)
