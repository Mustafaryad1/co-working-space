from django.db import models

# Create your models here.


class Space(models.Model):
    name = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    contacts = models.CharField(max_length=200)  # 30
    owner = models.ForeignKey('auth.User', related_name='spaces', on_delete=models.CASCADE)
    long = models.FloatField()
    lat = models.FloatField()
    # description = models.CharField(max_length=2000)
    air_conditioner = models.BooleanField(default=False)
    open_place = models.BooleanField(default=False)
    drinks_foods = models.BooleanField(default=False)
    laptop_tablet = models.BooleanField(default=False)
    parking = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class Event(models.Model):
    name = models.CharField(max_length=200)
    date = models.DateTimeField()
    number_of_people = models.IntegerField()
    space = models.ForeignKey(Space, related_name='events', on_delete=models.CASCADE)
    # start_date = models.DateTimeField()
    # end_date = models.DateTimeField()


class Room(models.Model):
    number = models.IntegerField()
    photo = models.FileField(upload_to='room/photos/')  # delete this
    space = models.ForeignKey(Space, related_name='rooms', on_delete=models.CASCADE)

# class SpaceImages(models.Model):

#     def validate_image(fieldfile_obj):
#         filesize = fieldfile_obj.file.size
#         megabyte_limit = 1.0
#         if filesize > megabyte_limit*1024*1024:
#             raise ValidationError("Max file size is %sMB" % str(megabyte_limit))

#     space = models.ForeignKey('Space',related_name='images',on_delete=models.CASCADE)
#     image = models.ImageField(upload_to='media/room/%Y/%m/%d/',validators=[validate_image])


class UserRate(models.Model):
    space = models.ForeignKey('Space', related_name='users_rates', on_delete=models.CASCADE)
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    feedback = models.CharField(max_length=2000)
    created = models.DateTimeField(auto_now=True)
    location = models.DecimalField(max_digits=2, decimal_places=1, default=0)
    internet = models.DecimalField(max_digits=2, decimal_places=1, default=0)
    clean = models.DecimalField(max_digits=2, decimal_places=1, default=0)
    calm = models.DecimalField(max_digits=2, decimal_places=1, default=0)
    staff = models.DecimalField(max_digits=2, decimal_places=1, default=0)

    class Meta:
        unique_together = (("user", "space"),)
