from django.contrib import admin

from .models import Rsvp


class RsvpAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'rsvp_code', 'responded', 'attending', 'updated_date')
    search_fields = ('name', 'rsvp_code', 'rsvp_code_slug',)
    ordering = ('-updated_date',)


admin.site.register(Rsvp, RsvpAdmin)
