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
        not_attending = responded.filter(attending=False)
        onsite = attending.filter(staying_onsite=True)
        friday = attending.filter(staying_friday=True)
        print """
Responded: {responded_count} / {total_count}
Attending: {attending_count} / {responded_count}
Confirmed guests: {confirmed_guests}
Confirmed guests on site: {confirmed_onsite}
Unconfirmed guests: {unconfirmed_guests}
        """.format(
            attending_count=attending.count(),
            confirmed_friday=sum_attribute(friday, 'confirmed_party_size'),
            confirmed_guests=sum_attribute(attending, 'confirmed_party_size'),
            confirmed_onsite=sum_attribute(onsite, 'confirmed_party_size'),
            responded_count=responded.count(),
            total_count=rsvps.count(),
            unconfirmed_guests=sum_attribute(not_responded, 'party_size')
        )
