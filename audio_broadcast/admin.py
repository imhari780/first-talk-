from django.contrib import admin
from . import models

# Automatically register all models in this app
for model in models.__dict__.values():
    if hasattr(model, "_meta"):
        try:
            admin.site.register(model)
        except admin.sites.AlreadyRegistered:
            pass
