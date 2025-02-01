from rest_framework.generics import RetrieveUpdateDestroyAPIView
from .models import ToDo
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from rest_framework.permissions import IsAuthenticated
from .serializers import ToDoSerializer
from rest_framework.response import Response
from rest_framework.views import APIView

from rest_framework_simplejwt.exceptions import TokenError
from django.conf import settings
from rest_framework_simplejwt.tokens import RefreshToken
from .authentication import CookieJWTAuthentication

# class ToDoListView(ListAPIView):
#     queryset = ToDo.objects.all()
#     serializer_class = ToDoSerializer

# class ToDoCreateView(CreateAPIView):
#     queryset = ToDo.objects.all()
#     serializer_class = ToDoSerializer

# Представление для чтения и создания записей
# class ToDoListCreateAPIView(ListCreateAPIView):
#     queryset = ToDo.objects.all().order_by('-checked', '-date_create')
#     serializer_class = ToDoSerializer
#     permission_classes = [IsAuthenticated]

class ToDoListCreateAPIView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request):
        return Response({'message': 'Это защищенный ресурс.'})
    
# Представление для обновления и удаления записи
class ToDoUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    queryset = ToDo.objects.all()
    serializer_class = ToDoSerializer
    permission_classes = [IsAuthenticated]















class ObtainTokenPairWithCookieView(TokenObtainPairView):
    def post(self, request, *args, **kwargs):
        response = super().post(request, *args, **kwargs)

        if response.status_code == 200:
            access_token = response.data['access']
            refresh_token = response.data['refresh']

            # Сохраняем токены в куки
            response.set_cookie(
                'access_token',
                access_token,
                max_age=settings.SIMPLE_JWT['ACCESS_TOKEN_LIFETIME'].total_seconds(),
                httponly=True,
                secure=False,  # Измените на True, если используете HTTPS
                samesite='Lax'
            )
            response.set_cookie(
                'refresh_token',
                refresh_token,
                max_age=settings.SIMPLE_JWT['REFRESH_TOKEN_LIFETIME'].total_seconds(),
                httponly=True,
                secure=False,  # Измените на True, если используете HTTPS
                samesite='Lax'
            )

        return response


class RefreshTokenWithCookieView(TokenRefreshView):
    def post(self, request, *args, **kwargs):
        refresh_token = request.COOKIES.get('refresh_token')

        if not refresh_token:
            return Response({'error': 'Refresh token not found'}, status=400)

        try:
            # Обновляем access-токен
            refresh = RefreshToken(refresh_token)
            access_token = str(refresh.access_token)

            # Создаем новый refresh-токен, если включено вращение
            if settings.SIMPLE_JWT['ROTATE_REFRESH_TOKENS']:
                new_refresh_token = str(refresh)
                response = Response({'access': access_token})
                response.set_cookie(
                    'refresh_token',
                    new_refresh_token,
                    max_age=settings.SIMPLE_JWT['REFRESH_TOKEN_LIFETIME'].total_seconds(),
                    httponly=True,
                    secure=False,  # Измените на True, если используете HTTPS
                    samesite='Lax'
                )
            else:
                response = Response({'access': access_token})

            # Обновляем access-токен в куках
            response.set_cookie(
                'access_token',
                access_token,
                max_age=settings.SIMPLE_JWT['ACCESS_TOKEN_LIFETIME'].total_seconds(),
                httponly=True,
                secure=False,  # Измените на True, если используете HTTPS
                samesite='Lax'
            )

            return response

        except TokenError as e:
            return Response({'error': str(e)}, status=400)
        
class LogoutView(APIView):
    def post(self, request, *args, **kwargs):
        response = Response({'message': 'Logged out successfully'})
        response.delete_cookie('access_token')
        response.delete_cookie('refresh_token')
        return response


class CheckTokenView(APIView):
    authentication_classes = [CookieJWTAuthentication]

    def get(self, request, *args, **kwargs):
        return Response({'message': 'Token is valid'}, status=200)