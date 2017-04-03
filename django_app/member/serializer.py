"""
Serialize to view user list made by custom user model (MyUser).
커스텀 유저 모델(MyUser)로 생성된 이용자 목록을 직렬화한다.
"""
from django.contrib.auth.models import Group
from rest_framework import serializers

from .models import MyUser


class UserSerializer(serializers.ModelSerializer):
    """
    Serialize user list.
    이용자 목록 직렬화.
    """

    def create(self, validated_data):
        user = MyUser.objects.create(
            email=validated_data['email'],
            nickname=validated_data['nickname']
        )
        user.set_password(validated_data['password'])
        user.save()

        return user

    class Meta:
        model = MyUser
        fields = ('url', 'email', 'nickname', 'password')


class GroupSerializer(serializers.ModelSerializer):
    """
    Serialize user Group.
    이용자 그룹 직렬화.
    """
    class Meta:
        model = Group
        fields = ('url', 'name')
