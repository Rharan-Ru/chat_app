from django.contrib import admin
from .models import ThreadModel, MessageModel, SolicitaModel
# Register your models here.

admin.site.register(ThreadModel)
admin.site.register(MessageModel)
admin.site.register(SolicitaModel)
