from django.contrib import admin

from .models import User, Hashtag


admin.site.register(User)
admin.site.register(Hashtag)