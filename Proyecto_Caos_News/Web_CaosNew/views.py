from ast import Not
import email
from multiprocessing import context
from urllib import response
from django.shortcuts import render
#importar modelo de socio
from .models import Socio
#Importar modelo de tablas del user
from django.contrib.auth.models import User
#importar librerias que validan el ingreso o login
from django.contrib.auth import authenticate,logout,login as login_aut
# Create your views here.

import requests
API_KEY= 'ee8732814db546feadf663f6271e6867'

def Home(request):
    return render(request,"Home.html")

def Galeria(request):
    return render(request,"Galeria.html")

def Registro(request):
    contexto = {"msg":""}
    if request.POST:
        n = request.POST.get("txtNombre")
        p = request.POST.get("txtContra")
        c = request.POST.get("txtCorreo")
        usu = User()
        usu.username = n
        usu.email = c
        usu.first_name = n
        usu.set_password(p)
        usu.save()
        contexto = {"msg":"Guardado"}
        return render(request,"Login.html",contexto)
    return render(request,"Registro.html",contexto)

def AgregarNoticia(request):
    return render(request,"AgregarNoticia.html")

def cerrar_sesion(request):
    logout(request)
    return render(request,"Home.html")

def Login(request):
    contexto={"msg":""}
    if request.POST:
        usuario = request.POST.get("txtCorreo")
        contra = request.POST.get("txtContra")
        print(usuario)
        print(contra)
        us = authenticate(request,username=usuario,password=contra)
        if us is not None and us.is_active :
            login_aut(request,us)
            return render(request,'Home.html',)
        else:
            contexto={"msg":"usuario o contraseña incorrecto"}
    return render(request,"Login.html",contexto)

def Contacto(request):
    return render(request,"Contacto.html")

def Cultural(request):
    return render(request,"Cultural.html")

def Nacional(request):
    return render(request,"Nacional.html")

def Regional(request):
    return render(request,"Regional.html")

def Educacional(request):
    return render(request,"Educacional.html")

def Noticia1(request):
    return render(request,"noticias/noticia1.html")

def Noticia2(request):
    return render(request,"noticias/noticia2.html")

def Noticia3(request):
    return render(request,"noticias/noticia3.html")

def Noticia4(request):
    return render(request,"noticias/noticia4.html")

def Noticia5(request):
    return render(request,"noticias/noticia5.html")

def Noticia6(request):
    return render(request,"noticias/noticia6.html")

def BuscaNoticia(request):
    Query = request.POST.get("Query")
    if Query:
        url =f'https://newsapi.org/v2/everything?q={Query}&language=es&sortby=popularity&apikey={API_KEY}'
        response = requests.get(url)
        data=response.json()
        articles = data['articles']

    else:
        Query="1hola"
        url =f'https://newsapi.org/v2/everything?q={Query}&language=es&sortby=popularity&apikey={API_KEY}'
        response = requests.get(url)
        data=response.json()
        articles = data['articles']

    context = {
        'articles' : articles,
    }
    return render(request,"BuscaNoticia.html",context)