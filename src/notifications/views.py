from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import User
from .services import deliver_notification
from .serializers import NotificationSerializer


class SendNotificationView(APIView):

    def get_serializer(self):
        return NotificationSerializer()

    def post(self, request):
        serializer = NotificationSerializer(data=request.data)
        if serializer.is_valid():
            message = serializer.validated_data['message']
            users = User.objects.all()
            for user in users:
                deliver_notification(user, message)
            return Response({"status": "Notification sent", "text": message}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)