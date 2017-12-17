from rest_framework.decorators import detail_route
from rest_framework.response import Response
from rest_framework import viewsets, permissions
from .models import Child, Log, Group
from .serializers import ChildSerializer, GroupSerializer, LogSerializer


class ChildViewSet(viewsets.ModelViewSet):
    queryset = Child.objects.filter(is_studying=True)
    serializer_class = ChildSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, permissions.DjangoModelPermissions)


class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, permissions.DjangoModelPermissions)


class LogViewSet(viewsets.ModelViewSet):
    queryset = Log.objects.all()
    serializer_class = LogSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, permissions.DjangoModelPermissions)
