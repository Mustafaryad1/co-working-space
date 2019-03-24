from . import views
from django.urls import path

urlpatterns = [
    path('spaces/',
         views.SpaceList.as_view(),
         name=views.SpaceList.name),
    path('spaces/<int:pk>/',
         views.SpaceDetial.as_view(),
         name=views.SpaceDetial.name),
    path('events/',
         views.EventList.as_view(),
         name=views.EventList.name),
    path('events/<int:pk>/',
         views.EventDetial.as_view(),
         name=views.EventDetial.name),
    path('rooms/',
         views.RoomList.as_view(),
         name=views.RoomList.name),
    path('rooms/<int:pk>/',
         views.RoomDetial.as_view(),
         name=views.RoomDetial.name),
    path('',
         views.ApiRoot.as_view(),
         name=views.ApiRoot.name),
    path('auth-system',
         views.RestAuth.as_view(),name='auth-system')
]
