from rest_framework import serializers
from .models import Space, Event, Room, UserRate


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
        exclude = ('long', 'lat')


class SpaceLocationSerializer(serializers.ModelSerializer):

    class Meta:
        model = Space
        fields = ('pk', 'name', 'long', 'lat')


class UserRateSerializer(serializers.ModelSerializer):
    space = serializers.ReadOnlyField(source='space.name')
    user = serializers.ReadOnlyField(source='user.username')

    class Meta:
        model = UserRate
        fields = ('__all__')


class RateSpaceSerializer(serializers.ModelSerializer):
    space = serializers.ReadOnlyField()
    user = serializers.ReadOnlyField()

    class Meta:
        model = UserRate
        fields = ('__all__')
