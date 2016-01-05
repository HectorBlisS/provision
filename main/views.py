# -*- encoding: utf-8 -*-
from django.shortcuts import render, redirect
from django.views.generic import View, TemplateView
from .forms import preguntaForm
from django import forms
from seguimiento.models import Size, Plazo
from django.core.mail import send_mail

class HomeView(View):
	def get(self,request):
		template_name="main/index.html"
		form=preguntaForm
		form.size=forms.ModelChoiceField(queryset=Size.objects.all(),empty_label=True)
		context={
			"form":form
		}

		return render(request,template_name,context)

	def post(self,request):
		form=preguntaForm(request.POST)
		if form.is_valid():
			pregunta=form.save()
			send_mail(
				'Sistema Terrenos',
				'Probando el envio automatico de Email. BlisS',
				'hola@fixter.org',
				['pro_vision@hotmail.com'], fail_silently=False
				)
			return redirect('_home')
			

		else:
			template_name="main/index.html"
			context={
			"form":form
			}
			return render(request,template_name,context)
