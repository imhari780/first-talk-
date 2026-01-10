from django.contrib import admin
from . import models

# register all models automatically (safe)
for model in models.__dict__.values():
    if hasattr(model, "_meta"):
        admin.site.register(model)
