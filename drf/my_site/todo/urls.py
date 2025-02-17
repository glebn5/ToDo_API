from django.urls import path
from .views import *
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView


urlpatterns = [
    # path('get/', ToDoListView.as_view()),
    # path('post/', ToDoCreateView.as_view()),
    path('tasks/', ToDoListCreateAPIView.as_view()),
    path('task/<int:pk>/', ToDoUpdateDestroyView.as_view()),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('register/', Register.as_view(), name="register"),
    path('logout/', LogoutView.as_view(), name='auth_logout'),
]

