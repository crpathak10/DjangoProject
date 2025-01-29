from rest_framework import serializers
from .models import UserDetails

class UserDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserDetails
        fields = ['username', 'email', 'password']

    
    def create(self, validated_data):
        user = UserDetails(**validated_data)
        user.password = validated_data['password']  # You can add hashing logic here
        user.save()
        return user

    def update(self, instance, validated_data):
        instance.username = validated_data.get('username', instance.username)
        instance.email = validated_data.get('email', instance.email)
        if validated_data.get('password'):
            instance.password = validated_data['password']  # Hashing can be added here
        instance.save()
        return instance
