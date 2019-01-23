from django.urls import path

from .views import Home, Notification

urlpatterns = [
    path('', Home.as_view(), name='chat_home'),
    path('notification/', Notification.as_view())
]
