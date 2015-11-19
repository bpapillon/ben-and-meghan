from django.conf import settings
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views.generic import TemplateView

from .forms import RsvpForm


class LocationView(TemplateView):
    template_name = 'location.html'

    def get_context_data(self, *args, **kwargs):
        context = super(LocationView, self).get_context_data(*args, **kwargs)
        context['google_maps_api_key'] = settings.GOOGLE_MAPS_API_KEY
        return context


def rsvp_view(request):
    if request.method == 'POST':
        form = RsvpForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = RsvpForm()
    return render(request, 'rsvp.html', {'form': form})
