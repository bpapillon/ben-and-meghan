from optparse import make_option

from django.core.management.base import BaseCommand

from wedding.models import Rsvp


class Command(BaseCommand):

    option_list = BaseCommand.option_list + (
        make_option('--first-name', '-f', action='store',
                    dest='first_name', help='First name'),
        make_option('--last-name', '-l', action='store',
                    dest='last_name', help='Last name'),
        make_option('--email', '-e', action='store',
                    dest='email', help='Email'),
        make_option('--party-size', '-p', action='store',
                    dest='party_size', help='Email'),
    )

    def handle(self, *args, **options):
        defaults = {}
        for attr in ('first_name', 'last_name', 'party_size',):
            if options[attr]:
                defaults[attr] = options[attr]
        obj, created = Rsvp.objects.update_or_create(email=options['email'], defaults=defaults)
        if created:
            print 'created new record %s with rsvp code %s' % (obj.email, obj.rsvp_code)
        else:
            print 'updated existing record %s with rsvp code %s' % (obj.email, obj.rsvp_code)
