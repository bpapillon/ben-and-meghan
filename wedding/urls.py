from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib import admin

from .views import HomeView, rsvp_view


urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^rsvp/(?P<rsvp_code>[\w\-]+)/', rsvp_view, name='rsvp'),
    url(r'^', HomeView.as_view(), name='home'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
