from django.contrib import admin
from .models import Departamento
from .models import CategoriaMaterial
from .models import Biblioteca
from .models import MaterialBibliografico
from .models import Prestamo

admin.site.register(Departamento)
admin.site.register(CategoriaMaterial)
admin.site.register(Biblioteca)

