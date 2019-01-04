from django import template
from chat.models import Room

register = template.Library()


@register.simple_tag
def get_main_message():
    room = Room.objects.get(group_name='main')
    old_messages = room.messages.order_by('-created')[:50]
    return old_messages
