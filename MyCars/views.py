from django.forms import ModelForm, modelform_factory
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect, render
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.base import View
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from .models import Cars
from .models import User

# Create your views here.
class index(View):
    def get(self, request, *args, **kwargs):
        cars = Cars.objects.all()
        return render(request, 'MyCars/inicio.html', {"cars" : cars})
    

class loginView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'MyCars/login.html')

    def post(self, request, *args, **kwargs):
        username = request.POST.get("username")
        password = request.POST.get("psw")
        user = authenticate(request, username = username, password = password)
        if (user is not None):
            login(request, user)
            return HttpResponseRedirect(reverse_lazy('MyCars:home'))
        else:
            messages.success(request, "Usuário não cadastrado.")
            HttpResponseRedirect(reverse_lazy('MyCars:cadastro'))

    def sair(request):
        logout(request)
        return HttpResponseRedirect(reverse_lazy('MyCars:home'))

class cadastro(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'MyCars/cadastro.html')

    def post(self, request, *args, **kwargs):
        context = {}
        username = request.POST.get("username")
        password = request.POST.get("psw")
        email = request.POST.get("email")
        User.objects.create(username = username, password = password, email = email)
        context['username'] = username
        context['password'] = password
        context['email'] = email

        return HttpResponseRedirect(reverse_lazy('MyCars:login'))

class apagar_carro(View):
    def get(self, request, pk, *args, **kwargs):
        car = Cars.objects.get(pk = pk)
        return render(request, 'MyCars/apagar_carro.html', {'car' : car})

    def post(self, request, pk, *args, **kwargs):
        car = Cars.objects.get(pk = pk)
        car.delete()
        return HttpResponseRedirect(reverse_lazy("MyCars:home"))

class editCar(View):
    def get(self, request, pk, *args, **kwargs):
        car = Cars.objects.get(pk=pk)
        return render(request, 'MyCars/cadastroCarro.html', {'car' : car})

    def post(self, request, pk, *args, **kwargs):
        car = get_object_or_404(Cars, pk=pk)
        # formulario = (request.POST, instance=car)

        # if formulario.is_valid():
        #     car = formulario.save()
        #     car.save()
        #     return HttpResponseRedirect(reverse_lazy("MyCars:home"))
        # else:
        #     contexto = {'car': formulario, }
        return render(request, 'MyCars/cadastroCarro.html')
    