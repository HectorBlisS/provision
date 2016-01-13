# -*- encoding: utf-8 -*-
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import View, TemplateView
from main.forms import preguntaForm
from django.core.mail import send_mail
from .models import NuevaPregunta, Size
from django import forms
from provision import settings
from datetime import datetime
from django.utils import formats

from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

# Login
from django.contrib.auth import authenticate,login, logout
from django.contrib.auth.decorators import permission_required
from django.core.urlresolvers import reverse

from django.utils import timezone

# Create your views here.
# class SeguiIndex(View):
# 	def get(self,request):
# 		template='seguimiento/index.html'
# 		# context={}
# 		return render(request,template)

# class SeguiStatus(TemplateView):

class SeguiStatus(View): # _inicio

	@method_decorator(permission_required("auth.adm", login_url='_home'))
	def get(self,request):
		preguntas=NuevaPregunta.objects.all().order_by('-pk')
		context={"mensajes":preguntas}
		template_name="seguimiento/clientes.html"
		return render(request,template_name,context)

class Revisar(View):
	@method_decorator(permission_required("auth.adm"),)
	def get(self,request,id):
		print ("entro al get")
		template_name="seguimiento/revisar.html"
		mensaje=get_object_or_404(NuevaPregunta,pk=id)
		context={
		"mensaje":mensaje
		}
		return render(request,template_name,context)
		
	def post(self,request,id):
		# print ("entro al post")
		msj=get_object_or_404(NuevaPregunta,pk=id)
		msj.nombre=request.POST.get("nombre","")
		# print("el nombre",msj.nombre)
		msj.tel=request.POST.get("tel","")
		msj.mail=request.POST.get("mail","")
		msj.comentario=request.POST.get("coment","")
		# Formateamos la fecha
		fecha=request.POST.get("contacto","")
		print(fecha)
		# print("sin formato: ",fecha)
		if fecha!="None":
			try:
				formateada = datetime.strptime(fecha, '%d %B, %Y')
			except:
				formateada=datetime.strptime(fecha,'%b. %d, %Y')
			# print("formateada: ",formateada)
			msj.contacto=formateada
		# msj.nombre=request.POST.get("state","")
		# if fecha==None:
		# 	formateada="None"
		# 	msj.contacto=formateada
		msj.save()
		return redirect("_inicio")

class RecibeGracias(View):
	def get(self,request):
		template="main/gracias.html"
		return render(request,template)

	def post(self,request):
		form=preguntaForm(request.POST)
		if form.is_valid():
			# Aqui guardamos en la base de datos asi de facil
			pregunta=form.save()
			# Bajamos el mail del cliente
			cliente_mail=form.data["mail"]
			cliente_name=form.data["nombre"]
			cliente_tel=form.data["tel"]
			cliente_tam=form.data["size"]
			cliente_plazo=form.data["plazo"]
			mensaje='Miguel, Tienes una nueva cotización pendiente DESDE PROVISION. http://www.pro-vision.com.mx/seguimiento/inicio/\n'
			mensaje+='Nombre: '+str(cliente_name)
			mensaje+='\nTelefono: '+str(cliente_tel)
			mensaje+='\nCorreo: '+str(cliente_mail)
			mensaje+='\nTamaño: '+str(cliente_tam)
			mensaje+='\nPlazo: '+str(cliente_plazo)
			# Notificamos a miguel
			send_mail(
				'Sistema Terrenos',
				mensaje,
				'sistema@fixter.org',
				['tterrenofacil@gmail.com'], fail_silently=False
				)
			# agradecemos al cliente y enviamos info
			send_mail(
				'Gracias por tu interez!',
				'Pronto te haremos una llamada.',
				'tterrenofacil@gmail.org',
				[cliente_mail], fail_silently=False
				)
			return redirect('_recibe')

			

		else:
			template_name="main/index.html"
			context={
			"form":form
			}
			return render(request,template_name,context)
class TakeForm(View):
	def get(self,request):
		template="main/gracias.html"
		return render(request,template)

	def post(self,request):
		nombre=request.POST.get("name","")
		nombre+=" - PVision"
		telefono=request.POST.get("tel","")
		mail=request.POST.get("mail","")
		size=request.POST.get("size","")
		plazo=request.POST.get("plazo")

		newPregunta=NuevaPregunta(
			nombre=nombre,
			tel=telefono,
			mail=mail,
			size=size,
			plazo=plazo,
			)
		newPregunta.save()
	# Notificamos a miguel
		mensaje='Miguel, Tienes una nueva cotización pendiente DESDE PROVISION. http://www.pro-vision.com.mx/seguimiento/inicio/\n'
		mensaje+='Nombre: '+nombre.encode("utf-8")
		mensaje+='\nTelefono: '+str(telefono)
		mensaje+='\nCorreo: '+str(mail)
		mensaje+='\nTamaño: '+str(size)
		mensaje+='\nPlazo: '+str(plazo)
		send_mail(
			'Sistema Terrenos',
			mensaje,
			'sistema@fixter.org',
			['tterrenofacil@gmail.com'], fail_silently=False
			)	
	# agradecemos al cliente y enviamos info
		send_mail(
			'Gracias por tu interez!',
			'Pronto te haremos una llamada.',
			'tterrenofacil@gmail.org',
			[mail], fail_silently=False
			)
		return redirect('_daform')


class Login(View):
	def get(self,request):
		template="seguimiento/login.html"
		if request.user.is_authenticated():
			return redirect("_inicio")
		else:
			# mensaje=""
			return render(request,template)


class TerrenoFacilForm(View):

	def get(self,request):
		nombre=request.GET.get("nombre","")
		nombre+=" - TFacil"
		telefono=request.GET.get("tel","")
		mail=request.GET.get("mail","")
		size=request.GET.get("size","")
		plazo=request.GET.get("plazo")

		newPregunta=NuevaPregunta(
			nombre=nombre,
			tel=telefono,
			mail=mail,
			size=size,
			plazo=plazo,
			)
		newPregunta.save()
	# Notificamos a miguel
		mensaje='Miguel, Tienes una nueva cotización pendiente DESDE TERRENOFACIL http://www.pro-vision.com.mx/seguimiento/inicio/\n'
		mensaje+='Nombre: '+str(nombre)
		mensaje+='\nTelefono: '+str(telefono)
		mensaje+='\nCorreo: '+str(mail)
		mensaje+='\nTamaño: '+str(size)
		mensaje+='\nPlazo: '+str(plazo)

		send_mail(
			'Sistema Terrenos',
			mensaje,
			'hola@fixter.org',
			['tterrenofacil@gmail.com'], fail_silently=False
			)
	# agradecemos al cliente y enviamos info
		send_mail(
			'Gracias por tu interez!',
			'Pronto te haremos una llamada.',
			'tterrenofacil@gmail.org',
			[mail], fail_silently=False
			)
		return redirect("http://www.terrenofacil.com.mx/gracias.html")







