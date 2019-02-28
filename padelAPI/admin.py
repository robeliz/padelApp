from django.contrib import admin

# Register your models here.
from .models import Court
from .models import Reservation


admin.site.register(Court)
admin.site.register(Reservation)
