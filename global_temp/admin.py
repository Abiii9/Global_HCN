from django.contrib import admin
from .models import Year, Temperature

# Registering the models Year and Temerature to the admin interface.
admin.site.register(Year)
admin.site.register(Temperature)
