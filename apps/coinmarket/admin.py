from django.contrib import admin

from .models import Cryptocurrency, Rate

admin.site.register(Cryptocurrency)
admin.site.register(Rate)
