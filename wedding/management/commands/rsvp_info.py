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
        print """
Invitations responded: {invitations_responded} / {invitations_total}
Invitations attending: {invitations_attending} / {invitations_responded}
Confirmed guests: {guests_confirmed}
Confirmed guests on site: {guests_onsite}
Confirmed guests for Friday: {guests_friday}
Unconfirmed guests: {guests_unconfirmed}
        """.format(
            guests_confirmed=sum_attribute(attending, 'confirmed_party_size'),
            guests_friday=sum_attribute(friday, 'confirmed_party_size'),
            guests_onsite=sum_attribute(onsite, 'confirmed_party_size'),
            guests_unconfirmed=sum_attribute(not_responded, 'party_size'),
            invitations_attending=attending.count(),
            invitations_responded=responded.count(),
            invitations_total=rsvps.count(),
        )
