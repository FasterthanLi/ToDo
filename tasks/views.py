from rest_framework import generics
from .models import Task
from .permissions import IsAuthorOrReadOnly
from .serializers import TaskSerializer
from rest_framework.response import Response
from rest_framework import status


class TaskList(generics.ListAPIView):
    permission_classes = (IsAuthorOrReadOnly,)
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

    def get_queryset(self):
        return super().get_queryset().filter(author=self.request.user)

    def list(self, request):
        queryset = self.get_queryset()
        serializer = TaskSerializer(queryset, many=True, fields=('id', 'title', 'deadline'))
        return Response(serializer.data)


class TaskDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthorOrReadOnly,)  
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

    # def get_queryset(self):
    #     return super().get_queryset().filter(author=self.request.user)
    


