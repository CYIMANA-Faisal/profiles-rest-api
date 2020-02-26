from rest_framework.views import APIView
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authentication import TokenAuthentication

from . import serializers, models, permissions


class HelloApiView(APIView):
    """ test api view """
    serializer_class = serializers.HelloSerializer
    def get(self, request, format=None):
        """Return a list of APIview features"""
        an_apiview = [
            'Uses standard HTTP methods as functions (get, post, put, patch, delete)',
            'simillar to django standard views',
            'Gives you mosta conctrol over your application logic',
            'Is mapped to URl manually',
        ]
        return Response({'message':'Hello' , 'an_apiview':an_apiview})

    def post(self, request):
        """Create hello message with our message"""
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}'
            return Response({'message':message})
        else:
            return Response(
                serializer.errors, 
                status = status.HTTP_400_BAD_REQUEST
            )
    def put(self, request, pk=None):
        """Handles the updating of the object"""
        return Response({"method":'put'})
    
    def patch(self, request, pk=None):
        """Handle  a partial update of an object """
        return Response({'method':'patch'})

    def delete(self, request, pk=None):
        """ Handle deletion of specific objects"""
        return Response({'method':'delete'})
class HelloViewset(viewsets.ViewSet):
    "test api viewset"
    serializer_class = serializers.HelloSerializer
    def list(self, request):
        """Return a hello message"""
        a_viewset = [
            'Uses actions(list, create, retrieve, update, partialudpade)',
            'Automatically maps to URLS using routers',
            'provide more functionality with less code',
        ]
        return Response({'message':'hello', 'a_viewset': a_viewset})
    def create(self, request):
         """Create new hello message"""
         serializer = self.serializer_class(data = request.data)
         if serializer.is_valid():
             name = serializer.validated_data.get('name')
             message = f'Hello {name}!'
             return Response({'message':message})
                        
         else:
            return Response(
                serializer.errors,
                status = status.HTTP_400_BAD_REQUEST
            )
    def retieve(self, request, pk=None):
        # handle getting object with its ID
        return Response({'methode': 'GET'})

    def update(self, request, pk=None):
        # handle update of an object with secified ID
        return Response({'methode':'PUT'})

    def partial_update(self, request, pk=None):
        # handle update part of an object
        return Response({'method':'PATCH'})

    def destroy(self, request, pk=None):
        # handle deletion of an object
        return Response({'method': 'DELETE'})

class UserProfileViewSet(viewsets.ModelViewSet):
    # Handles creating and updating profiles.
    serializer_class = serializers.UserProfileSerializer
    queryset = models.UserProfile.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (permissions.UpdateOwnProfile,)


