from django.db import models
from django.utils.text import slugify

from .utils import generate_rsvp_code


class Rsvp(models.Model):
    name = models.CharField(max_length=128, blank=False, null=False)
    email = models.EmailField(max_length=256, blank=False, null=False)
    party_size = models.IntegerField(null=False, blank=False)
    attending = models.BooleanField(default=True, null=False)
    responded = models.BooleanField(default=False, null=False)
    rsvp_code = models.CharField(max_length=128, blank=False, null=False, unique=True, db_index=True)
    rsvp_code_slug = models.CharField(max_length=128, blank=False, null=False, unique=True, db_index=True)
    staying_onsite = models.BooleanField(default=False, null=False)
    staying_friday = models.BooleanField(default=False, null=False)

    def __unicode__(self):
        return u'%s (%s)' % (self.name, self.email)

    def generate_rsvp_code(self):
        rsvp_code = generate_rsvp_code()
        while self.__class__.objects.filter(rsvp_code=rsvp_code).count() > 0:
            rsvp_code = generate_rsvp_code()
        return rsvp_code

    def save(self, *args, **kwargs):
        if not self.rsvp_code:
            self.rsvp_code = generate_rsvp_code()
        self.rsvp_code_slug = slugify(self.rsvp_code)
        return super(Rsvp, self).save(*args, **kwargs)
