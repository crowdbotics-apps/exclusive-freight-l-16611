from rest_framework import authentication
from task_profile.models import TaskerProfile, InviteCode, CustomerProfile, Notification
from .serializers import (
    TaskerProfileSerializer,
    InviteCodeSerializer,
    CustomerProfileSerializer,
    NotificationSerializer,
)
from rest_framework import viewsets


class InviteCodeViewSet(viewsets.ModelViewSet):
    serializer_class = InviteCodeSerializer
    authentication_classes = (
        authentication.SessionAuthentication,
        authentication.TokenAuthentication,
    )
    queryset = InviteCode.objects.all()


class TaskerProfileViewSet(viewsets.ModelViewSet):
    serializer_class = TaskerProfileSerializer
    authentication_classes = (
        authentication.SessionAuthentication,
        authentication.TokenAuthentication,
    )
    queryset = TaskerProfile.objects.all()


class CustomerProfileViewSet(viewsets.ModelViewSet):
    serializer_class = CustomerProfileSerializer
    authentication_classes = (
        authentication.SessionAuthentication,
        authentication.TokenAuthentication,
    )
    queryset = CustomerProfile.objects.all()


class NotificationViewSet(viewsets.ModelViewSet):
    serializer_class = NotificationSerializer
    authentication_classes = (
        authentication.SessionAuthentication,
        authentication.TokenAuthentication,
    )
    queryset = Notification.objects.all()
