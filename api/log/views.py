
from allauth.socialaccount.providers.google.views import GoogleOAuth2Adapter
from allauth.socialaccount.providers.vk.views import VKOAuth2Adapter
from rest_auth.registration.views import SocialLoginView, RegisterView
from rest_framework.response import Response
from allauth.socialaccount.providers.oauth2.client import OAuth2Client

from .serializers import RegistrationSerializer


class GoogleAuthView(SocialLoginView):
    adapter_class = GoogleOAuth2Adapter
    client_class = OAuth2Client
    callback_url = 'localhost:8000'

    def get(self, request):
        # Получение Access Token и Code из запроса
        access_token = request.query_params.get('access_token')
        code = request.query_params.get('code')

        # Выполните необходимые действия с полученными данными

        # Верните ответ в виде JSON или выполните редирект на другую страницу
        return Response({'access_token': access_token, 'code': code})


class VKAuthView(SocialLoginView):
    adapter_class = VKOAuth2Adapter
    client_class = OAuth2Client
    callback_url = 'localhost:8000'

    def get(self, request):
        # Получение Access Token и Code из запроса
        access_token = request.query_params.get('access_token')
        code = request.query_params.get('code')

        # Выполните необходимые действия с полученными данными

        # Верните ответ в виде JSON или выполните редирект на другую страницу
        return Response({'access_token': access_token, 'code': code})


class RegisterAuthView(RegisterView):
    serializer_class = RegistrationSerializer

    def UserCreation(self, request):
        self.create(request)
