from django.urls import path
from .views import Home, HomeTag, PostDetail


urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('<str:tag>', HomeTag.as_view(), name='home_tag'),
    path('post/<int:pk>', PostDetail.as_view(), name='post_detail'),
]
