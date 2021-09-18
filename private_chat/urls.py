from django.urls import path
from .views import ListThreads, ThreadView, CreateThread


urlpatterns = [
    path('inbox/', ListThreads.as_view(), name='inbox'),
    path('thread/<int:pk>', ThreadView.as_view(), name='thread'),
    path('create_thread/<int:pk>', CreateThread.as_view(), name='create_thread'),
]