import string

from django.conf import settings
from django.core.mail import EmailMessage, EmailMultiAlternatives
from django.template.loader import render_to_string

from wedding.models import Rsvp, SentEmail


def send_email(path, to, from_email, bcc=None, context=None):
    context = context or {}
    subject = render_to_string('{}_subject.txt'.format(path), context).strip()
    body_text = render_to_string('{}_body.txt'.format(path), context).strip()
    body_html = render_to_string('{}_body.html'.format(path), context).strip()
    email = EmailMultiAlternatives(
        subject=subject,
        body=body_text,
        from_email=from_email,
        to=to,
        bcc=bcc,
    )
    email.attach_alternative(body_html, 'text/html')
    ret = email.send()
    SentEmail.objects.create(to=to, subject=subject, body_html=body_html, body_text=body_text)
    return ret


def send_rsvp_confirmation_email(rsvp_id):
    rsvp = Rsvp.objects.get(id=rsvp_id)
    body = string.Template("""
New RSVP from $name
---

Attending: $attending
Party size: $party_size
Staying on-site: $staying_onsite
Staying Friday: $staying_friday
Comments:
$comments
""").substitute({
        'attending': rsvp.attending,
        'comments': rsvp.comments,
        'name': rsvp.name,
        'party_size': rsvp.confirmed_party_size,
        'staying_friday': rsvp.staying_friday,
        'staying_onsite': rsvp.staying_onsite,
    })
    reply_to = rsvp.email or settings.EMAIL_HOST_USER
    EmailMessage(
        'New RSVP from %s' % rsvp.name,
        body,
        settings.EMAIL_HOST_USER,
        settings.RSVP_EMAIL_RECIPIENTS.split(','),
        reply_to=[reply_to],
    ).send()
