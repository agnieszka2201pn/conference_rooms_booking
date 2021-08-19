"""project1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from conference_room_booking.views import MainView, AddRoom, ShowRooms, DeleteRoom, ModifyRoom, ReserveRoom, ConferenceRoomDetails

urlpatterns = [
    path('admin/', admin.site.urls),
    path('rooms/', MainView.as_view()),
    path('room/new/', AddRoom.as_view()),
    path('rooms/all/', ShowRooms.as_view()),
    path('room/delete/<int:room_id>/', DeleteRoom.as_view()),
    path('room/modify/<int:room_id>/', ModifyRoom.as_view()),
    path('room/reserve/<int:room_id>/', ReserveRoom.as_view()),
    path('room/details/<int:room_id>/', ConferenceRoomDetails.as_view()),
]
