from django.conf import settings
from django.conf.urls.static import static
from django import urls
from django.urls import path
from . import views

from conversation.views import conversations, conversation
from django.contrib.auth import views as mainViews
from feed.views import feed, search
from notification.views import notifications
from conversation.api import api_add_message
from feed.api import api_add_oink, api_add_like
from oinkerprofile.views import oinkerprofile, follow_oinker, unfollow_oinker, followers, follows, edit_profile

urlpatterns = [
    path('', views.frontpage, name="frontpage"),
    path('signup/', views.signup, name="signup"),
    path('logout/', views.log_out, name="logout"),
    path('login/', mainViews.LoginView.as_view(template_name='core/login.html'), name="login"),
    path('notifications/', notifications, name='notifications'),
    path('feed/', feed, name='feed'),
    path('search/', search, name='search'),
    path('edit_profile/', edit_profile, name='edit_profile'),
    path('conversations/', conversations, name='conversations'),
    path('conversations/<int:user_id>/', conversation, name='conversation'),
    path('u/<str:username>/', oinkerprofile, name='oinkerprofile'),
    path('u/<str:username>/followers/', followers, name='followers'),
    path('u/<str:username>/follows/', follows, name='follows'),
    path('u/<str:username>/follow/', follow_oinker, name='follow_oinker'),
    path('u/<str:username>/unfollow/', unfollow_oinker, name='unfollow_oinker'),
    # API
    path('api/add_oink/', api_add_oink, name='api_add_oink'),
    path('api/add_like/', api_add_like, name='api_add_like'),
    path('api/add_message/', api_add_message, name='api_add_message'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


