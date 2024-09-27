from django.core.mail import EmailMultiAlternatives
from flowlance.settings import EMAIL_HOST_USER
from django.template.loader import render_to_string

#Ejemplo de uso

#send_email("juanjosedelapava@gmail.com","Subject","Este es un test del body")

#los atributos title y footer son opcionales, estos le son pasados al html enviado
def send_email(To, Subject, Body, title="",footer=""):
    context = {
            'title': title,
            'message': Body,
            'footer':footer
        }

    html_content = render_to_string("utils/Email_template.html",context)
    email_to_send = EmailMultiAlternatives(
        Subject,
        Body,
        EMAIL_HOST_USER,
        [To],
    )
    email_to_send.attach_alternative(html_content,"text/html")
    return email_to_send.send()