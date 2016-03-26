import optparse

from django.core.management.base import BaseCommand

from wedding.models import Rsvp


class Command(BaseCommand):

    option_list = BaseCommand.option_list + (
        optparse.make_option('--email', '-e', action='store', dest='email', help='Email'),
        optparse.make_option('--name', '-n', action='store', dest='name', help='Name'),
        optparse.make_option('--party-size', '-p', action='store', dest='party_size', help='Party size'),
    )

    def handle(self, *args, **options):
        defaults = {}
        for attr in ('name', 'party_size',):
            if options[attr]:
                defaults[attr] = options[attr]
        obj, created = Rsvp.objects.update_or_create(email=options['email'], defaults=defaults)
        if created:
            print 'created new record %s with rsvp code "%s"' % (obj.email, obj.rsvp_code)
        else:
            print 'updated existing record %s with rsvp code "%s"' % (obj.email, obj.rsvp_code)
