from rest_framework.views import APIView
from rest_framework.response import Response


class HelloApiView(APIView):
    """ test api view """

    def get(self, request, format=None):
        """Return a list of APIview features"""
        an_apiview = [
            'Uses standard HTTP methods as functions (get, post, put, patch, delete)',
            'simillar to django standard views',
            'Gives you mosta conctrol over your application logic',
            'Is mapped to URl manually',
        ]
        return Response({'message':'Hello' , 'an_apiview':an_apiview})