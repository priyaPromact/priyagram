from django.contrib import admin

# Register your models here.
from .models import Activity, User, Photo

admin.site.register(User)
admin.site.register(Activity)
admin.site.register(Photo)