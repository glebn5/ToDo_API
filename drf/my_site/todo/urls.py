from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ToDoView

router = DefaultRouter()
router.register(r'products', ToDoView)

urlpatterns = [
    path('', include(router.urls)),
]

