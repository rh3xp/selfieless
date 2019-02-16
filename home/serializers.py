from rest_framework import serializers
from .models import Users

class UsersSerializer(serializers.ModelSerializer):
	class Meta:
		model = Users
		fields = ('id', 'uname', 'email', 'passwd', 'profile_pic', 'created')
		read_only_fields = ('profile_pic', 'created')
			