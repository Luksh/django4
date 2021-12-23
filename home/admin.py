from django.contrib import admin

from home.models import Contact, Feedback

# Register your models here.

admin.site.register(Contact)
admin.site.register(Feedback)
admin.site.register(Information)
admin.site.register(Blog)