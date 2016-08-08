import csv
import optparse
import sys

from django.core.management.base import BaseCommand, CommandError

from wedding.models import Rsvp


def sum_attribute(objs, attr):
    return reduce(lambda accum, obj: accum + getattr(obj, attr), objs, 0)


class Command(BaseCommand):

    option_list = BaseCommand.option_list + (
        optparse.make_option(
            '--attending',
            '-a',
            action='store_true',
            dest='attending',
            help='List only attending RSVPs',
        ),
        optparse.make_option(
            '--unconfirmed',
            '-u',
            action='store_true',
            dest='unconfirmed',
            help='List only unconfirmed RSVPs',
        ),
    )

    def handle(self, *args, **options):
        rsvps = Rsvp.objects.all()
        if options['attending'] and options['unconfirmed']:
            raise CommandError('Cannot provide both \'attending\' and \'unconfirmed\' flags')
        fields = ['name', 'email']
        if options['unconfirmed']:
            rsvps = rsvps.filter(responded=False)
        elif options['attending']:
            rsvps = rsvps.filter(responded=True, attending=True)
            fields.append('confirmed_party_size')
        writer = csv.writer(sys.stdout)
        writer.writerow(fields)
        for rsvp in rsvps:
            print writer.writerow([getattr(rsvp, field) for field in fields])
