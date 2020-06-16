# juschat/urls.py
from django.conf.urls import include
from django.contrib import admin
from django.urls import path

from chat.views import index,room

urlpatterns = [
    path('admin/', admin.site.urls),
    path('chat/', include('chat.urls'), name='chat'), 
]