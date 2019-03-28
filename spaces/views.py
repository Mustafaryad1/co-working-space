from rest_framework import generics
from rest_framework.reverse import reverse
from rest_framework.response import Response
from rest_framework import permissions
from rest_framework.decorators import api_view

from .permissions import IsOwnerOrReadOnly, IsSpaceOwnerOrReadOnly
from .models import Space, Event, Room, UserRate
from .serializers import (SpaceSerializer, RoomSerializer,
                          EventSerializer, SpaceLocationSerializer,
                          UserRateSerializer, RateSpaceSerializer)
from. pagination import PaginationWithMaxlimit


class SpaceList(generics.ListAPIView):
    queryset = Space.objects.all()
    serializer_class = SpaceSerializer
    name = 'space-list'
    pagination_class = PaginationWithMaxlimit
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    search_fields = ('name', 'address')
    filterset_fields = ('name', 'address')
    ordering_fields = '__all__'


class SpaceLocationList(generics.ListAPIView):
    queryset = Space.objects.all()
    serializer_class = SpaceLocationSerializer
    name = 'spacelocation-list'
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


class UserRateList(generics.ListAPIView):
    queryset = UserRate.objects.all()
    serializer_class = UserRateSerializer
    name = 'user-rate-list'
    pagination_class = PaginationWithMaxlimit
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)


# @api_view(['POST'])
# def user_rate(request):
#     if request.methods == "POST":
#         serializer = RateSpaceSerializer(data = request.data)
#         if serializer.is_valid():
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


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
            'rates': reverse(UserRateList.name, request=request),
            'Locations': reverse(SpaceLocationList.name, request=request),
            'sign-up': reverse('rest_register', request=request),
            'Auth-System': reverse('auth-system', request=request),


        })
