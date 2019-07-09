from django.contrib import admin

# Register your models here.

from .models import Call
from yata.handy import timestampToDate


class CallAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'last_update', 'key']

    def last_update(self, instance):
        return timestampToDate(instance.timestamp)


admin.site.register(Call, CallAdmin)
