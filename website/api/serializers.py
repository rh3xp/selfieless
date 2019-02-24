from rest_framework import serializers
from home.models import User

class UserSerializer(serializers.ModelSerializer):
	class Meta:
		model = User
		fields = ('id', 'uname', 'email', 'passwd', 'profile_pic', 'created')
		read_only_fields = ('profile_pic', 'created')
			
