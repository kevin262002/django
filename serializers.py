from rest_framework import serializers
from members.models import Member


class MemberSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=25)
    password = serializers.CharField(max_length=25)

    def create(self, validated_data):
        return Member.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.username = validated_data.get('username', instance.username)
        instance.password = validated_data.get('password', instance.password)
        instance.save()
        return instance