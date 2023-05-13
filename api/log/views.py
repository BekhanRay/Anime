
from allauth.socialaccount.providers.google.views import GoogleOAuth2Adapter
from allauth.socialaccount.providers.vk.views import VKOAuth2Adapter
from django.shortcuts import redirect
from rest_auth.registration.views import SocialLoginView, RegisterView
from rest_framework.response import Response
from allauth.socialaccount.providers.oauth2.client import OAuth2Client

from .serializers import RegistrationSerializer


class GoogleAuthView(SocialLoginView):
    adapter_class = GoogleOAuth2Adapter
    client_class = OAuth2Client
    callback_url = 'localhost:8000'

    def get(self, request):
        # Редирект пользователя на страницу аутентификации Google
        client_id = '854288019179-b801qvtn8fqbo6illmgcpfe2vmcj15ft.apps.googleusercontent.com'  # Замените на свой идентификатор клиента Google
        redirect_uri = 'http://127.0.0.1:8000/api/v1/'  # Замените на ваш URL перенаправления
        google_auth_url = f'https://accounts.google.com/o/oauth2/v2/auth?client_id={client_id}&redirect_uri={redirect_uri}&response_type=code&scope=openid%20email'

        return redirect(google_auth_url)


class VKAuthView(SocialLoginView):
    adapter_class = VKOAuth2Adapter
    client_class = OAuth2Client
    callback_url = 'localhost:8000'

    def get(self, request):
        # Редирект пользователя на страницу аутентификации ВКонтакте
        client_id = '51640013'  # Замените на свой идентификатор клиента ВКонтакте
        redirect_uri = 'http://127.0.0.1:8000/api/v1'  # Замените на ваш URL перенаправления
        vk_auth_url = f'https://oauth.vk.com/authorize?client_id={client_id}&redirect_uri={redirect_uri}&response_type=code&scope=email'

        return redirect(vk_auth_url)



class RegisterAuthView(RegisterView):
    serializer_class = RegistrationSerializer

    def UserCreation(self, request):
        self.create(request)
