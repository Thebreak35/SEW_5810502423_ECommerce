from django.contrib import admin

# Register your models here.
from .models import profiles

class profileAdmin(admin.ModelAdmin):
	class Meta:
		model = profiles

admin.site.register(profiles, profileAdmin)