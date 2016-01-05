from django.contrib import admin
from .models import NuevaPregunta, Size, Plazo
from django.contrib.auth.models import Permission

admin.site.register(NuevaPregunta)
admin.site.register(Size)
admin.site.register(Plazo)
admin.site.register(Permission)
# Register your models here.
