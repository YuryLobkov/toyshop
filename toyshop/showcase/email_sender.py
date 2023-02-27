from django.core.mail import send_mail, EmailMessage
from django.conf import settings
from django.template.loader import get_template
from django.contrib.sites.shortcuts import get_current_site
from django.contrib.auth.models import User
from asgiref.sync import sync_to_async


# def send(subject, message, recipients):
# 	send_mail(
#     		subject=subject,
#     		message=message,
#     		from_email=settings.EMAIL_HOST_USER,
#     		recipient_list=recipients)
	

# @sync_to_async
def email_customer_order(request, user, to_email, order):
    subject = 'Your ToyShop order #' + str(order.id)
    data_context = {
        'user': user,
        'order': order,
        'domain':get_current_site(request).domain,
        'protocol': 'https' if request.is_secure() else 'http'
    }
    message = get_template('showcase/email_customer_order.html').render(data_context)
    email = EmailMessage(subject, message, to=[to_email])
    email.content_subtype = 'html'
    email.send()
    print('conf message sent')

# @sync_to_async
def email_admin_notification(request, user, order):
    staff_users_mail_qeryset = User.objects.filter(is_staff = 1, is_active = 1).all().values_list('email')
    staff_users_mail = []
    for i in staff_users_mail_qeryset:
         staff_users_mail.append(i[0])
    subject = 'New order ' + str(order.id) + ' by ' + str(user)
    data_context = {
        'user': user,
        'order': order,
        'domain':get_current_site(request).domain,
        'protocol': 'https' if request.is_secure() else 'http'
    }
    message = get_template('showcase/email_notification.html').render(data_context)
    email = EmailMessage(subject, message, to=staff_users_mail)
    email.content_subtype = 'html'
    email.send()
    print('notif message sent')

# TODO unify functions to make it DRY

def email_admin_feedback_notification(request, feedback):
    staff_users_mail_qeryset = User.objects.filter(is_staff = 1, is_active = 1).all().values_list('email')
    staff_users_mail = []
    for i in staff_users_mail_qeryset:
         staff_users_mail.append(i[0])
    subject = 'New feedback ' + str(feedback.id) + ' by ' + str(feedback.name)
    data_context = {
        'feedback': feedback,
        'domain':get_current_site(request).domain, # unused here, left for further unification
        'protocol': 'https' if request.is_secure() else 'http' # unused here, left for further unification
    }
    message = get_template('showcase/email_feedback_notification.html').render(data_context)
    email = EmailMessage(subject, message, to=staff_users_mail)
    email.content_subtype = 'html'
    email.send()
    print('notif message sent')