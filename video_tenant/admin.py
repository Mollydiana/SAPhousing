from django.contrib import admin
from video_tenant.models import Account, Rental, Picture

# Register your models here.
admin.site.register(Account)
admin.site.register(Rental)
admin.site.register(Picture)