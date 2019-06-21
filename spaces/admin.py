from django.contrib import admin
from .models import Space, Event, Room, UserRate, SpaceImages

# Register your models here.

admin.site.register(Space)
admin.site.register(Event)
admin.site.register(Room)
admin.site.register(UserRate)
admin.site.register(SpaceImages)
