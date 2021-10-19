from django.urls import path
from .views import ListThreads, ThreadView, CreateThread, Solicita, RemoveSolicita


urlpatterns = [
    path('inbox/', ListThreads.as_view(), name='inbox'),
    path('solicita/<int:pk>', Solicita.as_view(), name='solicita'),
    path('remove_solicita/<int:pk>', RemoveSolicita.as_view(), name='remove_solicita'),
    path('thread/<int:pk>', ThreadView.as_view(), name='thread'),
    path('create_thread/<int:pk>', CreateThread.as_view(), name='create_thread'),
]