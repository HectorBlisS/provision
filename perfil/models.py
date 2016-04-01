from django.db import models
from django.conf import settings

# el lote actual y desarrollo son 
# provisionales al modelo de lotes y pagos

class Perfil(models.Model):
	user=models.OneToOneField(settings.AUTH_USER_MODEL)
	direccion=models.TextField(null=True,blank=True)
	lote_actual=models.CharField(max_length=100,null=True,blank=True)
	desarrollo=models.CharField(max_length=100,null=True,blank=True)
	pagos=models.BooleanField(default=True)

	def __str__(self):
		return 'Perfil de {}'.format(self.user.username)




