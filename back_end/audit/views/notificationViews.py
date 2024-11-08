from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from ..models import Notification
from ..serializer.notificationSerializer import NotificationSerializer


class NotificationListView(generics.ListAPIView):
    queryset = Notification.objects.all()
    serializer_class = NotificationSerializer
    permission_classes = [IsAuthenticated]

class CreateNotificationView(generics.CreateAPIView):
    queryset = Notification.objects.all()
    serializer_class = NotificationSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        # Associe l'utilisateur connecté à la notification lors de la création
        serializer.save(user=self.request.user)

class GetNotificationView(generics.RetrieveAPIView):
    queryset = Notification.objects.all()
    serializer_class = NotificationSerializer
    permission_classes = [IsAuthenticated]
