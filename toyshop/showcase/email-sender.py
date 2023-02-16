from django.core.mail import send_mail, EmailMessage
from django.conf import settings
from django.template.loader import get_template

def send(subject, message, recipients):
	send_mail(
    		subject=subject,
    		message=message,
    		from_email=settings.EMAIL_HOST_USER,
    		recipient_list=recipients)
	


def email_customer_order(request, user, to_email, order):
    subject = 'Your ToyShop order' + order.id
    data_context = {
        'user': user,
        'order': order,
        'protocol': 'https' if request.is_secure() else 'http'
    }
    message = get_template('showcase/email_customer_order.html').render(data_context)
    email = EmailMessage(subject, message, to=[to_email])
    email.content_subtype = 'html'
    email.send()
