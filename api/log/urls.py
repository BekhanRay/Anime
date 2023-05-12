from django.conf.urls import url
from django.urls import path, include
from rest_framework import routers

from log.views import VKAuthView, GoogleAuthView

urlpatterns = [
    # path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('auth/', include('social_django.urls', namespace='social')),
    path('social-auth/google/', GoogleAuthView.as_view(), name='google-auth'),
    path('social-auth/vk/', VKAuthView.as_view(), name='vk-auth'),
    # path('auth/', include('rest_framework_social_oauth2.urls')),
]
