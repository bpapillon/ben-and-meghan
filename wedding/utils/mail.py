from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string

from wedding.models import SentEmail


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
