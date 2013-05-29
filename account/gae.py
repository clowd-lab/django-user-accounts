from google.appengine.api import mail

def send_mail(subject, body, sender, to):
	mail.send_mail(sender, to, subject, body)
