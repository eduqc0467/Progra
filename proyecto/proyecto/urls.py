
from django.contrib import admin
from django.urls import path



from Models.Alumno.views import FormularioAlumnoView
from Views.HomeView import  HomeView
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', HomeView.home , name='home'),
    path('pagina/',HomeView.pagina1, name='pagina1'),
    path('pagina2/<int:parametro1>',HomeView.pagina2, name='pagina2'),
    path('pagina3/<int:parametro1>/<int:parametro2>',HomeView.pagina3, name='pagina3'),
    path('formulario/',HomeView.formulario, name='formulario'),
    path('registrarAlumno/',FormularioAlumnoView.index,name='registrarAlumno'),
    path('guardarAlumno/',FormularioAlumnoView.procesar_formulario,name='guardarAlumno')
]
