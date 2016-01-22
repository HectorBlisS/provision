# -*- encoding: utf-8 -*-
from celery.task.schedules import crontab
from celery.decorators import periodic_task
from django.core.mail import send_mail
from .models import NuevaPregunta
from django.utils import timezone
from datetime import datetime
import datetime

# minute=0, hour='*/24'

@periodic_task(run_every=(crontab(minute=0, hour='*/24')), name="contactar", ignore_result=True)
def contactar():
	pass
	preguntas=NuevaPregunta.objects.all()
	hoy=datetime.date.today()
	mensaje=""
	# try:
	# 	formateada = datetime.strptime(hoy, '%d %B, %Y')
	# except:
	# 	formateada=datetime.strptime(hoy,'%b. %d, %Y')
	for pregunta in preguntas:
		if pregunta.contacto==hoy:
			mensaje+='Recuerda llamar HOY a: \n'
			mensaje+='\nNombre: '+str(pregunta.nombre)
			mensaje+='\nTeléfono: '+str(pregunta.tel)
			mensaje+='\nTamaño: '+str(pregunta.size)
			mensaje+='\nPlazo: '+str(pregunta.plazo)
			print("Enviando Mail")
			mail="contacto@fixter.org"
			send_mail(
			'PROBANDO LAS ALERTAS RECORDATORIO.',
			mensaje,
			'tterrenofacil@gmail.org',
			[mail], fail_silently=False
			)