from django.contrib import admin
from .models import Comps, OS, RAM, HDD, Monitor, CPU, User


# Register your models here.

admin.site.register(Comps)
admin.site.register(OS)
admin.site.register(RAM)
admin.site.register(HDD)
admin.site.register(Monitor)
admin.site.register(CPU)
admin.site.register(User)

