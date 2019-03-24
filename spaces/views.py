from rest_framework import generics
from rest_framework.reverse import reverse
from rest_framework.response import Response
from rest_framework import permissions

from .permissions import IsOwnerOrReadOnly, IsSpaceOwnerOrReadOnly
from .models import Space, Event, Room
from .serializers import SpaceSerializer, RoomSerializer, EventSerializer
from. pagination import PaginationWithMaxlimit


class SpaceList(generics.ListAPIView):
    queryset = Space.objects.all()
    serializer_class = SpaceSerializer
    name = 'space-list'
    pagination_class = PaginationWithMaxlimit
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)


class SpaceDetial(generics.RetrieveUpdateAPIView):
    queryset = Space.objects.all()
    serializer_class = SpaceSerializer
    name = 'space-detial'
    permission_classes = (permissions.IsAuthenticated, IsOwnerOrReadOnly)


class EventList(generics.ListCreateAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    name = 'event-list'
    pagination_class = PaginationWithMaxlimit
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, )


class EventDetial(generics.RetrieveUpdateDestroyAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    name = 'event-detial'
    permission_classes = (permissions.IsAuthenticated, IsSpaceOwnerOrReadOnly)


class RoomList(generics.ListCreateAPIView):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer
    name = 'room-list'
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, )


class RoomDetial(generics.RetrieveUpdateDestroyAPIView):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer
    name = 'room-detial'
    permission_classes = (permissions.IsAuthenticated, IsSpaceOwnerOrReadOnly)


class RestAuth(generics.GenericAPIView):
    name = 'rest-auth'

    def get(self, request, *args, **kwargs):
        return Response({
            'User-detial': reverse('rest_user_details', request=request),
            'log-in': reverse('rest_login', request=request),
            'log-out': reverse('rest_logout', request=request),
            'change-password': reverse('rest_password_change', request=request),
            'reset-password': reverse('rest_password_reset', request=request),
            'confirm-reset-password': reverse('rest_password_reset_confirm', request=request),



        })


class ApiRoot(generics.GenericAPIView):
    name = 'api-root'

    def get(self, request, *args, **kwargs):
        return Response({
            'Spaces': reverse(SpaceList.name, request=request),
            'Events': reverse(EventList.name, request=request),
            'Rooms': reverse(RoomList.name, request=request),
            'sign-up': reverse('rest_register', request=request),
            'Auth-System': reverse('auth-system', request=request),


        })
