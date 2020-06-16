from django.urls import re_path

from . import consumers

websocket_urlpatterns = [
    re_path(r'ws/chat/(?P<room_name>\w+)/$', consumers.ChatConsumer),   #routing listens on this particular path and is then handled by the chat consumer
                                                                        #chat consumer asynchonously handles the different events
]