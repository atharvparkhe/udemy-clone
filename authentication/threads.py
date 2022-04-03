import threading, random
from django.conf import settings
from django.core.mail import send_mail, EmailMessage
from django.template.loader import render_to_string

context = {}
email_from = settings.EMAIL_HOST_USER

class send_forgot_otp(threading.Thread):
    def __init__(self, email, otp):
        self.email = email
        self.otp = otp
        threading.Thread.__init__(self)
    def run(self):
        try:
            subject = "OTP to change password"
            context["otp"] = self.otp
            html_template = 'reset.html'
            html_message = render_to_string(html_template, context)
            msg = EmailMessage(subject, html_message, email_from, [self.email])
            msg.content_subtype = 'html'
            msg.send()
        except Exception as e:
                print(e)


class send_verification_email(threading.Thread):
    def __init__(self, email, otp):
        self.email = email
        self.otp = otp
        threading.Thread.__init__(self)
    def run(self):
        try:
            context["otp"] = self.otp
            subject = "OTP to verify the your Account"
            html_template = 'verify.html'
            html_message = render_to_string(html_template, context)
            msg = EmailMessage(subject, html_message, email_from, [self.email])
            msg.content_subtype = 'html'
            msg.send()
        except Exception as e:
            print(e)