from rest_framework import serializers

from .models import Rsvp


class RsvpSerializer(serializers.ModelSerializer):

    class Meta:
        model = Rsvp

    def validate_party_size(self, value):
        try:
            return int(value)
        except (TypeError, ValueError):
            raise serializers.ValidationError('Party size must be a number, ya dingus')
