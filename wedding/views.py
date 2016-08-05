import datetime

from django.conf import settings
from django.shortcuts import get_object_or_404
from django.views.generic import TemplateView

from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Rsvp
from .serializers import RsvpSerializer


class HomeView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)
        context.update({
            'DISPLAY_EMAIL': settings.DISPLAY_EMAIL,
            'GOOGLE_ANALYTICS_KEY': settings.GOOGLE_ANALYTICS_KEY,
            'rsvp_cutoff': datetime.datetime.now() > settings.RSVP_CUTOFF_DATE,
        })
        return context


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
