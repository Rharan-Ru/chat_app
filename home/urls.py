from django.urls import path
from .views import Home, HomeTag, PostDetail, RedirectURL, AddLikes, AddDeslikes, ProfileView


urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('cate/<str:tag>', HomeTag.as_view(), name='home_tag'),
    path('post/<int:pk>', PostDetail.as_view(), name='post_detail'),
    path('profile/<int:pk>', ProfileView.as_view(), name='profile'),
    path('', RedirectURL.as_view(), name='login_universal'),
    path('likes/add/<int:pk>', AddLikes.as_view(), name='like_post'),
    path('deslikes/add/<int:pk>', AddDeslikes.as_view(), name='deslike_post'),

]
