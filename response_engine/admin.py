from django.contrib import admin

# Register your models here.
from django.contrib import admin

# RESPONSE ENGINE is an abstract, stateless service.
# It does NOT persist data.
# Hence, no models are registered in admin panel.

admin.site.site_header = "Response Engine Admin"
admin.site.site_title = "Response Engine"
admin.site.index_title = "Abstract System Response Module"
from django.contrib import admin
from . import models

# Automatically register all models in this app
for model in models.__dict__.values():
    if hasattr(model, "_meta"):
        try:
            admin.site.register(model)
        except admin.sites.AlreadyRegistered:
            pass
