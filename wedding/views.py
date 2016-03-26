from django.shortcuts import get_object_or_404

from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Rsvp
from .serializers import RsvpSerializer


@api_view(['GET', 'PUT'])
def rsvp_view(request, rsvp_code=None):
    rsvp = get_object_or_404(Rsvp, rsvp_code_slug=rsvp_code)
    if request.method == 'GET':
        data = RsvpSerializer(rsvp).data
        return Response(data)
    elif request.method == 'PUT':
        serializer = RsvpSerializer(rsvp, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
