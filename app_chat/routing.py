from django.conf.urls import url
from django.urls import path

from . import consumers_async

websocket_urlpatterns = [
    path('ws/chat/<str:room_name>/', consumers_async.ChatConsumer),
]