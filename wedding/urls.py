from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib import admin
from django.views.generic import TemplateView

from wedding.views import rsvp_view

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^rsvp/(?P<rsvp_code>[\w\-]+)/', rsvp_view, name='rsvp'),
    url(r'^', TemplateView.as_view(template_name='index.html'), name='home'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
