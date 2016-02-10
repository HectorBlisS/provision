# -*- encoding: utf-8 -*-
from celery.task.schedules import crontab
from celery.decorators import periodic_task
from django.core.mail import send_mail
from .models import NuevaPregunta
from django.utils import timezone
from datetime import datetime
import datetime

# minute=0, hour='*/24'

@periodic_task(run_every=(crontab(minute=0, hour='8')), name="contactar", ignore_result=True)
def contactar():
	preguntas=NuevaPregunta.objects.all()
	hoy=datetime.date.today()
	mail="tterrenofacil@gmail.com"
	# try:
	# 	formateada = datetime.strptime(hoy, '%d %B, %Y')
	# except:
	# 	formateada=datetime.strptime(hoy,'%b. %d, %Y')
	for pregunta in preguntas:
		if pregunta.contacto==hoy:
			datos={
			'p':pregunta
			}
			email_miguel(datos)
		# 	mensaje=""
		# 	mensaje+='Recuerda llamar HOY a: \n'
		# 	mensaje+='\nNombre: '+str(pregunta.nombre)
		# 	mensaje+='\nTeléfono: '+str(pregunta.tel)
		# 	mensaje+='\nTamaño: '+str(pregunta.size)
		# 	mensaje+='\nPlazo: '+str(pregunta.plazo)
		# 	print("Enviando Mail")
			
		# 	send_mail(
		# 	'RECORDATORIO',
		# 	mensaje,
		# 	'tterrenofacil@gmail.org',
		# 	[mail], fail_silently=False
		# 	)

def email_miguel(datos):
	subject="Nuevo Cliente"
	to=['tterrenofacil@gmail.com']
	from_email='tterrenofacil@gmail.com'
	ctx=datos

	message=get_template("seguimiento/email/remember.html").render(Context(ctx))
	msg=EmailMessage(subject,message,to=to,from_email=from_email)
	msg.content_subtype='html'
	msg.send()


