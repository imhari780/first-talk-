# import json
# from channels.generic.websocket import AsyncWebsocketConsumer
# from asgiref.sync import sync_to_async
# from .models import Message

# class ChatConsumer(AsyncWebsocketConsumer):

#     async def connect(self):
#         self.room_id = self.scope["url_route"]["kwargs"]["room_id"]
#         self.group_name = f"room_{self.room_id}"

#         await self.channel_layer.group_add(self.group_name, self.channel_name)
#         await self.accept()

#     async def disconnect(self, close_code):
#         await self.channel_layer.group_discard(self.group_name, self.channel_name)

#     async def receive(self, text_data):
#         data = json.loads(text_data)
#         content = data.get("content")

#         if not content:
#             return

#         message = await self.save_message(content)

#         await self.channel_layer.group_send(
#             self.group_name,
#             {
#                 "type": "broadcast",
#                 "message": {
#                     "message_id": str(message.message_id),
#                     "room_id": str(message.room_id),
#                     "sender_id": str(message.sender_id),
#                     "timestamp": message.created_at.isoformat(),
#                     "content": message.content,
#                 },
#             }
#         )

#     async def broadcast(self, event):
#         await self.send(text_data=json.dumps(event["message"]))

#     @sync_to_async
#     def save_message(self, content):
#         return Message.objects.create(
#             room_id=self.room_id,
#             sender_id=self.scope["user"].user_id,
#             content=content
#         )

import json

from channels.generic.websocket import AsyncWebsocketConsumer


class ChatConsumer(AsyncWebsocketConsumer):

    async def connect(self):
        self.room_id = self.scope["url_route"]["kwargs"]["room_id"]
        self.group_name = f"chat_{self.room_id}"

        await self.channel_layer.group_add(self.group_name, self.channel_name)
        await self.accept()

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(self.group_name, self.channel_name)

    async def broadcast_message(self, event):
        await self.send(text_data=json.dumps(event["data"]))
