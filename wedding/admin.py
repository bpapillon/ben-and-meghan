from django.contrib import admin

from .models import Rsvp


class RsvpAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'rsvp_code', 'responded', 'attending')
    search_fields = ('name', 'rsvp_code', 'rsvp_code_slug',)


admin.site.register(Rsvp, RsvpAdmin)
