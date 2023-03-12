from django.contrib import admin
from . import models


@admin.register(models.Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ["name", "citizenship", "birth_year", "work_place"]


@admin.register(models.Account)
class AccountAdmin(admin.ModelAdmin):
    list_display = ["number", "account_type", "client"]


@admin.register(models.Credit)
class CreditAdmin(admin.ModelAdmin):
    list_display = ["sum", "date", "account"]
