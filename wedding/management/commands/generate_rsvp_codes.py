import optparse

from django.core.management.base import BaseCommand

from wedding.models import Rsvp


class Command(BaseCommand):

    option_list = BaseCommand.option_list + (
        optparse.make_option(
            '--overwrite',
            '-o',
            action='store_true',
            default=False,
            dest='overwrite',
            help='Overwrite existing RSVP codes',
        ),
    )

    def handle(self, *args, **options):
        rsvps = Rsvp.objects.all()
        if not options['overwrite']:
            rsvps = rsvps.filter(rsvp_code__isnull=True)
        for rsvp in rsvps:
            rsvp.rsvp_code = rsvp.generate_rsvp_code()
            rsvp.save()
