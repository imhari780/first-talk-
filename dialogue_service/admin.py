from django.contrib import admin

from .models import DialogueMessage, DialogueSession


@admin.register(DialogueSession)
class DialogueSessionAdmin(admin.ModelAdmin):
    pass


@admin.register(DialogueMessage)
class DialogueMessageAdmin(admin.ModelAdmin):
    pass
