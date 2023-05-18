from django.contrib import admin

from .models import Profile, Account, Transaction

admin.site.register(Profile)
# admin.site.register(Income)
admin.site.register(Transaction)
admin.site.register(Account)

