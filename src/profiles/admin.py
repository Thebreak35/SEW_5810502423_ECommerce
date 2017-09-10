from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.
from .models import profiles, userStripe

class profileAdmin(admin.ModelAdmin):
	class Meta:
		model = profiles

admin.site.register(profiles, profileAdmin) 

class userStripeAdmin(admin.ModelAdmin):
    class Meta:
        model = userStripe
admin.site.register(userStripe, userStripeAdmin)