from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from . import serializers


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