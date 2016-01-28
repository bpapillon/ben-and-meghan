from django.db import models

from .utils import generate_rsvp_code


class Rsvp(models.Model):
    first_name = models.CharField(max_length=128, blank=False, null=False)
    last_name = models.CharField(max_length=128, blank=False, null=False)
    email = models.EmailField(max_length=256, blank=False, null=False)
    party_size = models.IntegerField(null=False, blank=False)
    attending = models.BooleanField(default=True, null=False)
    responded = models.BooleanField(default=False, null=False)
    rsvp_code = models.CharField(max_length=128, blank=False, null=False, unique=True, db_index=True)

    def __unicode__(self):
        return u"%s %s (%s)" % (self.first_name, self.last_name, self.email)

    def generate_rsvp_code(self):
        rsvp_code = generate_rsvp_code()
        while self.__class__.objects.filter(rsvp_code=rsvp_code).count() > 0:
            rsvp_code = generate_rsvp_code()
        return rsvp_code

    def save(self, *args, **kwargs):
        if not self.rsvp_code:
            self.rsvp_code = generate_rsvp_code()
        return super(Rsvp, self).save(*args, **kwargs)
