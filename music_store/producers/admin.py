from django.contrib import admin
from producers.models import Producer


# Register your models here.

class ProducerAdmin(admin.ModelAdmin):
    list_display = ('name',)
    pass

admin.site.register(Producer, ProducerAdmin)
