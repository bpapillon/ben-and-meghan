from django.forms import ModelForm
from wedding.models import Rsvp


class RsvpForm(ModelForm):
    class Meta:
        model = Rsvp
        fields = ['first_name', 'last_name', 'email', 'party_size', 'attending']
