from rest_framework.generics import RetrieveUpdateDestroyAPIView, ListCreateAPIView
from .models import ToDo
from rest_framework.permissions import IsAuthenticated
from .serializers import *
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import logout

# class ToDoListView(ListAPIView):
#     queryset = ToDo.objects.all()
#     serializer_class = ToDoSerializer

# class ToDoCreateView(CreateAPIView):
#     queryset = ToDo.objects.all()
#     serializer_class = ToDoSerializer

# Представление для чтения и создания записей
class ToDoListCreateAPIView(ListCreateAPIView):
    queryset = ToDo.objects.all().order_by('checked', '-date_create')
    serializer_class = ToDoSerializer
    permission_classes = (IsAuthenticated,)

# class ToDoListCreateAPIView(APIView):
#     permission_classes = [IsAuthenticated]
#     def get(self, request):
#         return Response({'message': 'Это защищенный ресурс.'})
    
# Представление для обновления и удаления записи
class ToDoUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    queryset = ToDo.objects.all()
    serializer_class = ToDoSerializer
    # permission_classes = [IsAuthenticated]


class Register(APIView):
    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "User registered successfully!"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)




class LogoutView(APIView):
    def post(self, request, *args, **kwargs):
        # Удаляем токен или сессию пользователя
        logout(request)
        response = Response({"detail": "Successfully logged out."}, status=status.HTTP_200_OK)
        
        # Очищаем куки, если вы используете JWT или другие токены в куках
        response.delete_cookie('access_token')
        response.delete_cookie('refresh_token')
        return response