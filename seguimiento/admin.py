# -*- coding: utf-8 -*-
from django.contrib import admin
from .models import NuevaPregunta, Size, Plazo
from django.contrib.auth.models import Permission

# admin.site.register(NuevaPregunta)
admin.site.register(Size)
admin.site.register(Plazo)
admin.site.register(Permission)
# Register your models here.

class NuevaPreguntaAdmin(admin.ModelAdmin):
	list_display=('nombre','tel','cerrado')
	list_filter=('cerrado',)
	search_field=('title','date')
	date_hierarchy='date'
	ordering=['date']
admin.site.register(NuevaPregunta,NuevaPreguntaAdmin)
