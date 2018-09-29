from django.contrib import admin

from .models import Account, AccountActions


admin.site.register(Account)
admin.site.register(AccountActions)