from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib import admin
from django.views.generic import TemplateView

from wedding.views import LocationView, rsvp_view

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^accommodations/', TemplateView.as_view(template_name="accommodations.html"), name="accommodations"),
    url(r'^event_info/', TemplateView.as_view(template_name="event_info.html"), name="event_info"),
    url(r'^location/', LocationView.as_view(), name="location"),
    url(r'^rsvp/', rsvp_view, name="rsvp"),
    url(r'^registry/', TemplateView.as_view(template_name="registry.html"), name="registry"),
    url(r'^', TemplateView.as_view(template_name="home.html"), name="home"),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
