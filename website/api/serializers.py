from rest_framework import serializers
from home.models import User, Post, Category

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'uname', 'email', 'passwd', 'profile_pic', 'created')
        read_only_fields = ('profile_pic', 'created')


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'name')
        #read_only_fields = ('profile_pic', 'created')

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ('id', 'title', 'text')
