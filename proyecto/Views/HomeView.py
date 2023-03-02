from django.http import HttpResponse
from django.template.loader import get_template
from django.shortcuts import render





class HomeView():

    def my_view(request):
        return render(request, 'index.html')

    def home(self):
        plantilla = get_template('index.html')

        return HttpResponse(plantilla.render())

    def pagina1(self):
        return HttpResponse('holap')

    def pagina2(self,parametro1):
        return HttpResponse('Hola2' + str(parametro1))

    def pagina3(self, parametro1, parametro2):
        return HttpResponse('Hola nuevo' + str(parametro1)+'  -  ' + str(parametro2))

    def formulario(self):
        plantilla = get_template('formulario.html')
        return HttpResponse(plantilla.render())
