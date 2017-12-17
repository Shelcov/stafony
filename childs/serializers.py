from rest_framework import routers, serializers, viewsets
from django.contrib.auth.models import User
from .models import Child, Log, Group


class ChildSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Child
        fields = ('id', 'photo', 'name', 'gender', 'birthdate', 'group')


class LogSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Log
        fields = ('id', 'child', 'event_time', 'parent', 'event_type')


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('id', 'name',)
