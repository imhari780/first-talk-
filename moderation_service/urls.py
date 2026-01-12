from django.urls import path

from .views import mute_user, soft_delete_message, temp_block_user

urlpatterns = [
    path("mute/", mute_user),
    path("soft-delete/", soft_delete_message),
    path("temp-block/", temp_block_user),
]
