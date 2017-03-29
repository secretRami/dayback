from django.contrib.auth.models import Group
from rest_framework import permissions
from rest_framework import viewsets

from .models import MyUser
from .serializer import UserSerializer, GroupSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = MyUser.objects.all()
    serializer_class = UserSerializer
    # permission_classes = (IsAuthenticatedOrCreate, IsOwnerOrReadOnly)
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)


class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
