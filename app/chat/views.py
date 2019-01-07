from django.views.generic import TemplateView
from rest_framework.response import Response
from rest_framework.views import APIView

from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync

from chat.models import Room


class Home(TemplateView):
    template_name = 'index.html'

    def get(self, request, *args, **kwargs):
        Room.objects.get_or_create(name='노티룸', group_name='main')
        return super().get(request, *args, **kwargs)


def send_message(message):

    channel_layer = get_channel_layer()
    async_to_sync(channel_layer.group_send)(
        'main',
        {
            'type': 'chat_message',
            'message': str(message),
            'created': message.created.strftime('%p %I:%M')
        }
    )


class Notification(APIView):
    def post(self, request, *args, **kwargs):
        room = Room.objects.get(group_name='main')
        message = room.messages.create(message=request.data.get('message'))

        channel_layer = get_channel_layer()
        async_to_sync(channel_layer.group_send)(
            'main',
            {
                'type': 'chat_message',
                'message': str(message),
                'created': message.created.strftime('%p %I:%M')
            }
        )

        return Response({'status': 200, 'meesage': '{} send success'.format(message)})
