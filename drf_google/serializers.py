"""
    serializers
    ~~~~~~~~~~~

    Google related DRF serializers.
"""

from rest_framework import serializers
from .utils import places


class GooglePlacesForm(serializers.Serializer):
    """ GooglePlacesForm serializer """

    pid = serializers.CharField(max_length=100)

    def save(self, **kwargs):
        """ DRF Override to perform the Google Places query """

        return places(self.validated_data['pid'])
