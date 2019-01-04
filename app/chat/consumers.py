import json

from channels.generic.websocket import AsyncJsonWebsocketConsumer


class ChatConsumer(AsyncJsonWebsocketConsumer):
    async def connect(self):
        self.noti_group_name = 'main'

        await self.channel_layer.group_add(
            self.noti_group_name,
            self.channel_name
        )

        await self.accept()

    async def disconnect(self, code):
        await self.channel_layer.group_discard(
            self.noti_group_name,
            self.channel_name
        )

    async def chat_message(self, event):
        message = event['message']
        created = event['created']
        await self.send(text_data=json.dumps({
            'message': message,
            'created': created
        }))
