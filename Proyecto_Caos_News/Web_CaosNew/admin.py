#importar modelos
from django.contrib import admin
from .models import Categoria, Socio

# Register your models here.

admin.site.register(Categoria)
admin.site.register(Socio)