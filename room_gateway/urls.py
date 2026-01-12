from django.urls import path

from .views import create_room, join_room, leave_room

urlpatterns = [
    # CREATE ROOM
    path("rooms/create/", create_room),
    # JOIN ROOM (INTEGER room_id)
    path("rooms/<int:room_id>/join/", join_room),
    # LEAVE ROOM
    path("rooms/<int:room_id>/leave/", leave_room),
]
