# AUTHORISATION SERVER SERIALIZERS FILE
# ----------------------------------------------------------------------------------------------------------------------

from rest_framework import serializers
from django.contrib.auth.models import User


# User model serializer
class CreateUserSerializer(serializers.ModelSerializer):
    
    # The create method overrides the default class when saving data for a user, this is important to make sure the password is hashed correctly
    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user
    
    # The metadata include the details of a user, that is each has an id a username and a password
    class Meta:
        model = User
        fields = ('id', 'username', 'password')
        extra_kwargs = {
            'password': {'write_only': True}
        }