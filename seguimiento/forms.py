from django import forms
from .models import DatoExtra



class ExtraForm(forms.ModelForm):
	class Meta:
		model = DatoExtra
		fields = ['dato',]