from django.shortcuts import render
from django.views.generic import View
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

class DashBoard(View):
	@method_decorator(login_required(login_url='perfil:login'))
	def get(self,request):
		template=('perfil/dashboard.html')
		context={

		}
		return render(request,template,context)