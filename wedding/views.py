from django.core.urlresolvers import reverse
from django.http import Http404
from django.shortcuts import redirect, render

from .forms import RsvpCodeForm, RsvpForm
from .models import Rsvp


def home_view(request):
    if request.method == 'POST':
        rsvp_code = request.POST.get('rsvp_code')
        if rsvp_code is None:
            raise Http404()
        try:
            rsvp = Rsvp.objects.get(rsvp_code=rsvp_code.replace(' ', '-'))
        except Rsvp.DoesNotExist:
            raise Http404()
        return redirect(reverse('rsvp', args=(rsvp.rsvp_code,)))
    else:
        form = RsvpCodeForm()
    return render(request, 'home.html', {'form': form})


def rsvp_view(request, rsvp_code):
    try:
        obj = Rsvp.objects.get(rsvp_code=rsvp_code)
    except Rsvp.DoesNotExist:
        raise Http404()
    if request.method == 'POST':
        form = RsvpForm(request.POST, instance=obj)
        if form.is_valid():
            obj = form.save()
    else:
        form = RsvpForm(instance=obj)
    return render(request, 'rsvp.html', {'form': form, 'obj': obj})
