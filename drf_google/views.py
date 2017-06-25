"""
    views
    ~~~~~

    Common DRF views for interacting with Google
"""

from rest_framework.generics import GenericAPIView
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
from .serializers import GooglePlacesForm


class GooglePlacesView(GenericAPIView):
    """ Google Places API View """

    renderer_classes = (JSONRenderer,)
    parser_classes = (JSONParser,)
    serializer_class = GooglePlacesForm

    def post(self, request):
        """ Query the Google Places API by placeId """

        serializer = self.get_serializer(data=self.request.data)
        serializer.is_valid(raise_exception=True)
        return Response(serializer.save())
