from rest_framework import serializers

from . models import Profile
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        field = ['username','email',]


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserSerializer()
        field = ['full_name','phone','gender','profile_pix']


class RegistrationSerializer(serializers.ModelSerializer):
    username = serializers.CharField(write_only = True)
    password = serializers.CharField(write_only = True)
    password1 = serializers.CharField(write_only = True)
    email = serializers.EmailField(write_only = True)

    class Meta:
        model = Profile
        fields = ['full_name','phone','gender','profile_pix','email','username','password','password1']
    def validate(self,data):
        if data['password'] != data['password1']:
            raise serializers.ValidationError('password does not match')
        return data
    
    def create(self, validated_data):
        username = validated_data.pop('username')
        email = validated_data.pop('email')
        password = validated_data.pop('password')

        user = User.objects.create_user(username=username,email=email,password=password)

        profile = Profile.objects.create(
            user = user,
            full_name = validated_data['full_name'],
            phone = validated_data['phone'],
            gender= validated_data['gender'],
            profile_pix = validated_data.get('profile_pix'),
        )
        return profile




