from django.db import models


class Rsvp(models.Model):
    first_name = models.CharField(max_length=128, blank=False, null=False)
    last_name = models.CharField(max_length=128, blank=False, null=False)
    email = models.EmailField(max_length=256, blank=False, null=False)
    party_size = models.IntegerField(null=False, blank=False)
    attending = models.BooleanField(default=True, null=False)
