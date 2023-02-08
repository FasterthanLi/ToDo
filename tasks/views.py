from rest_framework import generics
from .models import Task
from .permissions import IsAuthorOrReadOnly
from .serializers import TaskSerializer
from rest_framework.response import Response
from .tasks import send_email_task
from django.conf import settings


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

    def get_queryset(self):
        return super().get_queryset().filter(author=self.request.user)
    
    def post(self, request, pk):
        task = Task.objects.get(id=pk)
        task.completed = not task.completed
        task.save()

        author_email = task.author.email
        if author_email:
            subject = "Task status update"
            message = "Task has been marked as completed" if task.completed else "Task has benn un-marked as completed"
            from_email = settings.EMAIL_BACKEND
            recipient_list = [author_email]
            fail_silently=True

            send_email_task.delay(subject, message, from_email, recipient_list)
            return Response({"status": "success"})
        else:
            return Response({"status": "error", "message": "Author email address not found"})
    