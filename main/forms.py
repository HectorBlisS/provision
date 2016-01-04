from django import forms
from django.forms import ModelForm, Select
from seguimiento.models import NuevaPregunta, Size, Plazo
from django.forms import widgets

class preguntaForm(forms.ModelForm):
	class Meta:
		model=NuevaPregunta
		fields=(
			'nombre',
			'tel',
			'mail',
			'size',
			'plazo',
			)
		# fields = '__all__'
		field_classes=("browser-default",)

		widgets = {
		# 'size': Select(attrs={'class': "browser-default",}),
		# 'plazo':Select(attrs={'class':'browser-default',})
		}
		labels={
			'size':'¿De cuantos m2 quieres tu terreno?',
			'nombre':'Escribe tu Nombre',
			'tel':'Teléfono celular o local',
			'mail':'Tu Correo electrónico',
			'plazo':'¿A que plazo quieres pagarlo?'
		}
