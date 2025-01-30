from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import *



urlpatterns = [
    # path('get/', ToDoListView.as_view()),
    # path('post/', ToDoCreateView.as_view()),
    path('tasks/', ToDoListCreateAPIView.as_view()),
    path('task/<int:pk>/', ToDoUpdateDestroyView.as_view())
]

