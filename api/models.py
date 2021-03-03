from django.db import models

CATEGORY_CHOICES = (
  ('marketing_digital','Marketing Digital'),
  ('manualidades','Manualidades'),
  ('ilustraciones_dibujo','Ilustraciones y Dibujo'),
  ('lifestyle','Lifestyle'),
  ('video','Video'),
  ('negocios','Negocios'),
  ('fotografia','Fotografía'),
  ('diseño','Diseño'),
  ('escritura','Escritura'),
  ('animacion_3D','Animación & 3D'),
)
SUBCATEGORY_CHOICES = (
  ('marketing_digital','Marketing Digital'),
  ('bordado_costura','Bordado y costura'),
  ('ilustraciones_digital','Ilustraciones Digital'),
  ('lifestyle','Lifestyle'),
  ('produccion','Producción'),
  ('video','Video'),
  ('diseño','Diseño'),
  ('locucion','Locución'),
  ('escritura','Escritura'),
  ('animacion_2D','Animación 2D'),
  ('innovacion','Innovación'),
  ('liderazgo','Liderazgo'),
  ('fundamentos_fotografia','Fundamentos de fotografia'),
  ('publicidad','Publicidad'),
  ('postproduccion','Postroduccion'),
  ('dibujo','Dibujo'),
  ('branding','Branding'),
  ('retoque_fotografico','Retoque Fotográfico'),
  ('data','Data'),
  ('ventas','Ventas'),
)

LEVEL_CHOICES = (
  ('avanzado','Avanzado'),
  ('Introductorio','Introductorio'),
  ('completo','Completo'),
  ('intermedio','Intermedio'),
)

class Course(models.Model):
  name = models.CharField(max_length=150)
  level = models.CharField(max_length=50, choices=LEVEL_CHOICES)
  category_name =  models.CharField(max_length=150, choices=CATEGORY_CHOICES)
  subcategory_name = models.CharField(max_length=150, choices=SUBCATEGORY_CHOICES)
  username = models.CharField(max_length=50)
  real_price = models.FloatField(default=5)
  price = models.FloatField(default=5)
  discount = models.IntegerField(default=30)
  course_score = models.FloatField(default=3.5)
  users = models.IntegerField(default=0)
