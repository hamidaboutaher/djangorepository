from django.contrib import admin
from .models import Meeting, Minutes, resouce, Event

# Register your models here.
# Necessary if they are to appear in the admin
admin.site.register(Meeting)
admin.site.register(Minutes)
admin.site.register(resouce)
admin.site.register(Event)

# Register your models here.
