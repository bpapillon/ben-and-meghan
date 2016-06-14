from django.core.management.base import BaseCommand

from wedding.models import Rsvp


def sum_attribute(objs, attr):
    return reduce(lambda accum, obj: accum + getattr(obj, attr), objs, 0)


class Command(BaseCommand):

    def handle(self, *args, **options):
        rsvps = Rsvp.objects.all()
        responded = rsvps.filter(responded=True)
        not_responded = rsvps.filter(responded=False)
        attending = responded.filter(attending=True)
        onsite = attending.filter(staying_onsite=True)
        friday = attending.filter(staying_friday=True)
        attendance_rate = float(attending.count()) / float(responded.count())
        guests_confirmed = sum_attribute(attending, 'confirmed_party_size')
        guests_unconfirmed = sum_attribute(not_responded, 'party_size')
        print """
Invitations responded: {invitations_responded} / {invitations_total}
Invitations attending: {invitations_attending} / {invitations_responded}
Confirmed guests: {guests_confirmed}
Confirmed guests on site: {guests_onsite}
Confirmed guests for Friday: {guests_friday}
Unconfirmed guests: {guests_unconfirmed}
Max possible guests: {guests_max}
Estimated total guests: {guests_estimated}
        """.format(
            guests_confirmed=guests_confirmed,
            guests_estimated=guests_confirmed + int(attendance_rate * guests_unconfirmed),
            guests_friday=sum_attribute(friday, 'confirmed_party_size'),
            guests_max=guests_confirmed + guests_unconfirmed,
            guests_onsite=sum_attribute(onsite, 'confirmed_party_size'),
            guests_unconfirmed=guests_unconfirmed,
            invitations_attending=attending.count(),
            invitations_responded=responded.count(),
            invitations_total=rsvps.count(),
        )
