import json

from channels.generic.websocket import SyncConsumer
from django.template.loader import render_to_string


class ChatConsumer(SyncConsumer):
    def websocket_connect(self, event):
        self.send({"type": "websocket.accept"})

    def disconnect(self, close_code):
        pass

    def websocket_receive(self, event):
        print(self, event, event["text"])
        msg = json.loads(event["text"])
        template_name = "live_edit/message.html"
        context = {
            "message": msg["chatmessage"],
            "message_id": "333",
        }  # Your context variables
        rendered_string = render_to_string(template_name, context)
        self.send({"type": "websocket.send", "text": rendered_string})
