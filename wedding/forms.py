from django import forms
from wedding.models import Rsvp


class RsvpForm(forms.ModelForm):
    responded = forms.BooleanField(widget=forms.HiddenInput(), initial=True)
    class Meta:
        model = Rsvp
        fields = [
            'first_name',
            'last_name',
            'email',
            'party_size',
            'attending',
            'responded',
        ]


class RsvpCodeForm(forms.ModelForm):
    class Meta:
        model = Rsvp
        fields = [
            'rsvp_code',
        ]
