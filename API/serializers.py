from rest_framework import serializers
from .models import Post
from django.contrib.auth.models import User

class PostSerializer(serializers.ModelSerializer):

    image = serializers.ImageField(max_length=None, use_url=True)

    class Meta:
        model = Post
        fields = ['id', 'name', 'country', 'description', 'popularPlaces', 'image']

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email', 'password']
        extra_kwargs = {'password' : {'write_only' : True}}

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user