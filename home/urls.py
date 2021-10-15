from django.urls import path
from .views import Home, HomeTag, PostDetail, RedirectURL, AddLikes


urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('<str:tag>', HomeTag.as_view(), name='home_tag'),
    path('post/<int:pk>', PostDetail.as_view(), name='post_detail'),
    path('login', RedirectURL.as_view(), name='login_universal'),
    path('likes/add/<int:pk>', AddLikes.as_view(), name='like_post'),

]
