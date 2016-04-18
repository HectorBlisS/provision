# -*- coding: utf-8 -*-
from django.contrib import admin
from .models import DatoExtra, NuevaPregunta, Size, Plazo, Actualizacion
from django.contrib.auth.models import Permission

# admin.site.register(NuevaPregunta)
admin.site.register(Size)
admin.site.register(Plazo)
admin.site.register(Permission)
admin.site.register(Actualizacion)
# Register your models here.

class DatoExtraInline(admin.TabularInline):
	model=DatoExtra
	raw_id_fields=['pregunta']

class NuevaPreguntaAdmin(admin.ModelAdmin):
	list_display=('nombre','tel','cerrado')
	list_filter=('cerrado',)
	search_field=('title','date','mail')
	date_hierarchy='date'
	ordering=['date']
	inlines=[DatoExtraInline]

admin.site.register(NuevaPregunta,NuevaPreguntaAdmin)


