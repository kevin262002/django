from rest_framework import serializers
from members.models import Member

class MemberSerializer(serializers.Serializer):
    firstname = serializers.CharField(max_length=25)
    lastname = serializers.CharField(max_length=25)
    city = serializers.CharField(max_length=20)
    
    def create(self, validated_data):
        return Member.objects.create(**validated_data)
    
    def update(self, instance, validated_data):
        instance.firstname = validated_data.get('firstname', instance.firstname)
        instance.lastname = validated_data.get('lastname', instance.lastname)
        instance.city = validated_data.get('city', instance.city)
        instance.save()
        return instance



    