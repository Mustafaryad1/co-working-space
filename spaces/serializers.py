from rest_framework import serializers
from .models import Space, Event, Room


class EventSerializer(serializers.ModelSerializer):
    space = serializers.ReadOnlyField(source='space.name')

    class Meta:
        model = Event
        fields = ('pk', 'name', 'space', 'date', 'number_of_people')


class RoomSerializer(serializers.ModelSerializer):
    space = serializers.ReadOnlyField(source='space.name')

    class Meta:
        model = Room
        fields = ('pk', 'photo', 'number', 'space')


class SpaceSerializer(serializers.ModelSerializer):
    events = EventSerializer(many=True, read_only=True)
    rooms = RoomSerializer(many=True, read_only=True)
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Space
        fields = ('name','owner','pk', 'location', 'contacts', 'events', 'rooms')
