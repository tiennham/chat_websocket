from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.security.websocket import AllowedHostsOriginValidator
from django.urls import path, re_path

from chat.consumers import ChatConsumer
from notification.consumers import NotificationConsumer
from public_chat.consumers import PublicChatConsumer

application = ProtocolTypeRouter({
    'websocket': AllowedHostsOriginValidator(
        AuthMiddlewareStack(
            URLRouter([
                path('public_chat/<room_id>/', PublicChatConsumer),  # this same on the lesson but not working on local
                # path('public_chat/<room_id>/', PublicChatConsumer.as_asgi()), # this trick on stackoverflow
                # path('chat/<room_id>/', ChatConsumer.as_asgi()),
                path('chat/<room_id>/', ChatConsumer),
                # path('', NotificationConsumer.as_asgi()),
                path('', NotificationConsumer.as_asgi()),
            ])
        )
    ),
})
