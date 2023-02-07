from rest_framework.decorators import api_view
from .tasks import send_email
from rest_framework.response import Response


@api_view(['GET'])
def view_function(request):
    send_email.delay('recipient@example.com', 'Subject', 'Message')
    return Response({'message': 'Email sent'})