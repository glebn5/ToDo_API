from rest_framework.generics import RetrieveUpdateDestroyAPIView, ListCreateAPIView
from .models import ToDo
from rest_framework.permissions import IsAuthenticated
from .serializers import ToDoSerializer

# class ToDoListView(ListAPIView):
#     queryset = ToDo.objects.all()
#     serializer_class = ToDoSerializer

# class ToDoCreateView(CreateAPIView):
#     queryset = ToDo.objects.all()
#     serializer_class = ToDoSerializer

# Представление для чтения и создания записей
class ToDoListCreateAPIView(ListCreateAPIView):
    queryset = ToDo.objects.all().order_by('-checked', '-date_create')
    serializer_class = ToDoSerializer
    permission_classes = [IsAuthenticated]
# Представление для обновления и удаления записи
class ToDoUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    queryset = ToDo.objects.all()
    serializer_class = ToDoSerializer
