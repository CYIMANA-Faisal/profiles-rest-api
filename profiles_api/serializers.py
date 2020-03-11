from rest_framework import serializers
from profiles_api import models

class HelloSerializer(serializers.Serializer):
    """Serialises a name field for testing our API"""
    name = serializers.CharField(max_length = 10)


class UserProfileSerializer(serializers.ModelSerializer):
    """ Serialiises a user profile object """
    class Meta:
        model = models.UserProfile
        fields = ('id', 'email', 'name', 'password')
        extra_kwargs = {
            'password' : {
                'write_only' : True,
                'style' : {'input_type':'password'}
            } 
        }
    def create(self, validated_data):
        # create and return new user
        user = models.UserProfile.objects.create_user(
            email = validated_data['email'],
            name = validated_data['name'],
            password= validated_data['password']
        )
        return user


class ProfileFeedSerializer(serializers.ModelSerializer):
    # Serializer profile feed Items

    class Meta:
        model = models.ProfileFeedItem
        fields = ('id', 'user_profile', 'status_text', 'created_on', )
        extra_kwargs = {
             'user_profile':{
                 'read_only':True
             } 
        }
