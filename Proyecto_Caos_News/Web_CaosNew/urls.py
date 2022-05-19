from django.contrib import admin
from django.urls import path
from .views import Home,cerrar_sesion,BuscaNoticia, Galeria, Registro, Login, AgregarNoticia, Contacto, Cultural, Educacional, Nacional, Regional, Noticia1, Noticia2, Noticia3, Noticia4, Noticia5, Noticia6

urlpatterns = [
    path('', Home,name='HOME'),
    path('BuscaNoticia/', BuscaNoticia,name='BUSCA'),
    path('Galeria/', Galeria,name='GALE'),
    path('Registro/', Registro,name='REGIS'),
    path('AgregarNoticia/', AgregarNoticia,name='AGRE'),
    path('Login/', Login,name='LOGI'),
    path('Contacto/', Contacto,name='CONT'),
    path('Cultural/', Cultural,name='CULT'),
    path('Educacional/', Educacional,name='EDUC'),
    path('Nacional/', Nacional,name='NACI'),
    path('Regional/', Regional,name='REGI'),
    path('Noticia1/', Noticia1,name='NOT1'),
    path('Noticia2/', Noticia2,name='NOT2'),
    path('Noticia3/', Noticia3,name='NOT3'),
    path('Noticia4/', Noticia4,name='NOT4'),
    path('Noticia5/', Noticia5,name='NOT5'),
    path('Noticia6/', Noticia6,name='NOT6'),
    path('Cerrar/', cerrar_sesion,name='CERRAR'),
]
