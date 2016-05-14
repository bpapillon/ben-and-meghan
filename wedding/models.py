from django.db import models
from django.db.models import Q
from django.utils import timezone

from .utils.rsvp_code import generate_rsvp_code


class Rsvp(models.Model):
    name = models.CharField(max_length=128, blank=False, null=False)
    email = models.EmailField(max_length=256, blank=True, null=True)
    party_size = models.IntegerField(null=False, blank=False)
    attending = models.BooleanField(default=True, null=False)
    responded = models.BooleanField(default=False, null=False)
    rsvp_code = models.CharField(max_length=128, blank=True, null=True, unique=True, db_index=True)
    rsvp_code_slug = models.CharField(max_length=128, blank=True, null=True, unique=True, db_index=True)
    staying_onsite = models.BooleanField(default=False, null=False)
    staying_friday = models.BooleanField(default=False, null=False)
    updated_date = models.DateTimeField(null=True, blank=True)
    created_date = models.DateTimeField(null=True, blank=True, auto_now_add=True)

    def __unicode__(self):
        return u'%s (%s)' % (self.name, self.email)

    def generate_rsvp_code(self):
        rsvp_code, rsvp_code_slug = generate_rsvp_code()
        while self.__class__.objects.filter(Q(rsvp_code=rsvp_code)|Q(rsvp_code_slug=rsvp_code_slug)).count() > 0:
            rsvp_code, rsvp_code_slug = generate_rsvp_code()
        return rsvp_code, rsvp_code_slug

    def save(self, *args, **kwargs):
        if not self.rsvp_code:
            self.rsvp_code, self.rsvp_code_slug = self.generate_rsvp_code()
        self.updated_date = timezone.now()
        return super(Rsvp, self).save(*args, **kwargs)


class SentEmail(models.Model):
    to = models.EmailField(max_length=256, blank=False, null=False)
    subject = models.CharField(max_length=256, blank=True, null=False)
    body_html = models.TextField(blank=True, null=False)
    body_text = models.TextField(blank=True, null=False)
    sent_date = models.DateTimeField(null=True, auto_now_add=True)
