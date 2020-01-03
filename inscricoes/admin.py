from django.contrib import admin

from .models import Usuario, \
                    TipoInscricao, \
                    Evento, \
                    Inscricao

# Register your models here.
admin.site.register(TipoInscricao)
admin.site.register(Inscricao)
admin.site.register(Evento)
admin.site.register(Usuario)
