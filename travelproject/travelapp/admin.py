from django.contrib import admin

# Register your models here.
from .models import place, Guides

admin.site.register(place)

admin.site.register(Guides)
