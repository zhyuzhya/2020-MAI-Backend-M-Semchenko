from django.contrib import admin
from profiles.models import Profile

# Register your models here.

class ProfileAdmin(admin.ModelAdmin):
    list_display = ('login', 'first_name', 'second_name', 'date_of_birth', 'email_address', 'password')
    pass

admin.site.register(Profile, ProfileAdmin)
