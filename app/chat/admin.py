from django.contrib import admin

from chat.models import Room, RoomMessage

admin.site.register(Room)
admin.site.register(RoomMessage)