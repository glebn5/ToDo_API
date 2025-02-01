from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import *
from rest_framework_simplejwt.views import TokenVerifyView


urlpatterns = [
    # path('get/', ToDoListView.as_view()),
    # path('post/', ToDoCreateView.as_view()),
    path('tasks/', ToDoListCreateAPIView.as_view()),
    path('task/<int:pk>/', ToDoUpdateDestroyView.as_view()),
    path('token/', ObtainTokenPairWithCookieView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', RefreshTokenWithCookieView.as_view(), name='token_refresh'),
    path('token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    path('check_token/', CheckTokenView.as_view()),
    path('logout/', LogoutView.as_view(),)
]

