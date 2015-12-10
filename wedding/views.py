from django.shortcuts import render

from .forms import RsvpForm


def rsvp_view(request):
    if request.method == 'POST':
        form = RsvpForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = RsvpForm()
    return render(request, 'rsvp.html', {'form': form})
