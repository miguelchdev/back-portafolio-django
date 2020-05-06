from django.core.mail import EmailMessage


def send_email(from_email, to_email, body, subject, reply_to):
    email = EmailMessage()
    email.subject = subject
    email.body = body
    email.from_email = from_email
    email.to = [to_email, ]
    if reply_to:
        email.reply_to = [reply_to, ]
    else:
        email.reply_to = [from_email, ]
    email.send()
