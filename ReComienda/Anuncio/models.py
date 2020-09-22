from django.db import models
#from django.contrib.auth.models import User
from usuario.models import Perfil
# Create your models here.

class Localidad(models.Model):
	localidad = models.CharField(max_length= 60)

	def __str__(self):
		return self.localidad

class Transporte(models.Model):
	transporte = models.CharField(max_length = 50)

	def __str__(self):
		return self.transporte

class Anuncio_Trans(models.Model):
	nombre = models.CharField(max_length=30)
	E_mail = models.EmailField(null=True)
	localidad_origen = models.ForeignKey(Localidad, on_delete = models.CASCADE, related_name = 'localidad_origen_trans')
	localidad_destino = models.ForeignKey(Localidad, on_delete = models.CASCADE, related_name = 'localidad_destino_trans')
	recorrido = models.TextField()	
	titulo = models.CharField(max_length=30)
	descripcion = models.TextField()
	transporte = models.ForeignKey(Transporte, on_delete = models.CASCADE)	
	usuario = models.ForeignKey(Perfil, on_delete=models.CASCADE, null=True)
	fecha_publicacion = models.DateTimeField(auto_now_add = True)
	fecha_caducidad = models.DateTimeField()
	telefono = models.CharField(null=True, max_length=20)
	permitir_comentarios = models.BooleanField(default = True)
	
	
	
	def __str__(self):
		return self.titulo

		
"""class Anuncio_Contra(models.Model):
	nombre = models.CharField(max_length=30)
	Email = models.EmailField(null=False)
	localidad_origen = models.ForeignKey(Localidad, on_delete = models.CASCADE, related_name = 'localidad_origen')
	localidad_destino = models.ForeignKey(Localidad, on_delete = models.CASCADE, related_name = 'localidad_destino')
	titulo = models.CharField(max_length=30)
	descripcion = models.TextField()
	#usuario
	fecha_publicacion = models.DateTimeField(auto_now_add = True)
	fecha_
	tel = models.IntegerField(null=False)
	
	
	
	def __str__(self):
		return self.titulo"""

class Contratista(models.Model):
	titulo = models.CharField(max_length=30)
	fecha_viaje = models.DateTimeField()
	fecha_lapso = models.DateTimeField()
	localidad_origen = models.ForeignKey(Localidad, on_delete = models.CASCADE, related_name = 'localidad_origen')
	localidad_destino = models.ForeignKey(Localidad, on_delete = models.CASCADE, related_name = 'localidad_destino')
	descripcion = models.TextField()
	usuario = models.ForeignKey(Perfil, on_delete=models.CASCADE, null=True)
	permitir_comentarios = models.BooleanField(default = True)	
	E_mail = models.EmailField(null=True)
	telefono = models.CharField(max_length=20, null=True, verbose_name="Nro Telefono")
	"""tipo_servicio = models.ForeignKey(Servicios, on_delete = models.CASCADE, null=True)"""

"""class Servicios(models.Model):
	nombre = models.CharField(max_length= 40)
	def __str__(self):
		return self.nombre"""

class Comentario(models.Model):
    anuncio=models.ForeignKey(Anuncio_Trans, on_delete = models.CASCADE)
    usuario=models.ForeignKey(Perfil, on_delete = models.SET_NULL, null=True)
    texto=models.TextField(max_length=200)
    fecha_creacion = models.DateTimeField(auto_now_add=True)