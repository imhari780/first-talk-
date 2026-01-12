# # Register your models here.
# from django.contrib import admin
# from response_engine.models import Prompt


# admin.site.register(Prompt)

# # RESPONSE ENGINE is an abstract, stateless service.
# # It does NOT persist data.
# # Hence, no models are registered in admin panel.

# admin.site.site_header = "Response Engine Admin"
# admin.site.site_title = "Response Engine"
# admin.site.index_title = "Abstract System Response Module"
# from django.contrib import admin
# from . import models

# # Automatically register all models in this app
# for model in models.__dict__.values():
#     if hasattr(model, "_meta"):
#         try:
#             admin.site.register(model)
#         except admin.sites.AlreadyRegistered:
#             pass
from django.contrib import admin
from . import models

# ===============================
# RESPONSE ENGINE ADMIN
# ===============================

admin.site.site_header = "Response Engine Admin"
admin.site.site_title = "Response Engine"
admin.site.index_title = "Abstract System Response Module"

# Automatically register all concrete models
for model in models.__dict__.values():
    if hasattr(model, "_meta") and not model._meta.abstract:
        try:
            admin.site.register(model)
        except admin.sites.AlreadyRegistered:
            pass
