from django.contrib import admin

from .models import Rsvp


class RsvpAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'rsvp_code', 'responded', 'attending', 'confirmed_party_size', 'updated_date')
    list_filter = ('attending', 'responded',)
    ordering = ('-updated_date',)
    search_fields = ('name', 'rsvp_code', 'rsvp_code_slug',)


admin.site.register(Rsvp, RsvpAdmin)
