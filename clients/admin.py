from django.contrib import admin
from .models import Client, Passport, PotentialClient, TelegramUser, TelegramUserLog

# @admin.register(Client)
# class ClientAdmin(admin.ModelAdmin):
#     list_display = ('first_name', 'last_name', 'phone', 'email', 'status', 'created_at')
#     search_fields = ('first_name', 'last_name', 'phone', 'email')
#     list_filter = ('status', 'gender', 'created_at')
#     ordering = ('created_at',)
#     fieldsets = (
#         ('Основная информация', {
#             'fields': ('first_name', 'last_name', 'middle_name', 'gender', 'phone', 'email', 'language')
#         }),
#         ('Детали клиента', {
#             'fields': ('client_id', 'source', 'status', 'other1', 'other2', 'credit_status', 'other_details')
#         }),
#         ('Время', {
#             'fields': ('created_at', 'updated_at')
#         }),
#     )
#     readonly_fields = ('created_at', 'updated_at')

# @admin.register(Passport)
# class PassportAdmin(admin.ModelAdmin):
#     list_display = ('client', 'passport_number', 'issue_date', 'expiry_date', 'issuing_authority')
#     search_fields = ('passport_number', 'client__first_name', 'client__last_name')
#     list_filter = ('issuing_authority',)

# @admin.register(PotentialClient)
# class PotentialClientAdmin(admin.ModelAdmin):
#     list_display = ('client_id', 'phone', 'contract_id', 'created_at')
#     search_fields = ('client_id', 'phone', 'contract_id')
#     list_filter = ('created_at',)

# @admin.register(TelegramUser)
# class TelegramUserAdmin(admin.ModelAdmin):
#     list_display = ('telegram_id', 'first_name', 'last_name', 'username', 'approved', 'created_at')
#     search_fields = ('telegram_id', 'phone_number', 'first_name', 'last_name', 'username')
#     list_filter = ('approved',)

# @admin.register(TelegramUserLog)
# class TelegramUserLogAdmin(admin.ModelAdmin):
#     list_display = ('user', 'action', 'timestamp')
#     search_fields = ('user__telegram_id', 'action')
#     list_filter = ('timestamp',)


# @admin.register(Client)
# @admin.register(Passport)
# @admin.register(PotentialClient)
# @admin.register(TelegramUser)
# @admin.register(TelegramUserLog)
# class ClientAdmin(admin.ModelAdmin):
#     pass

from django.contrib import admin
from .models import Client, Passport, PotentialClient, TelegramUser, TelegramUserLog

# Регистрация моделей
@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ['client_id', 'first_name', 'last_name', 'phone', 'email', 'status']
    search_fields = ['client_id', 'first_name', 'last_name', 'phone', 'email']

@admin.register(Passport)
class PassportAdmin(admin.ModelAdmin):
    list_display = ['client', 'passport_number', 'issue_date', 'expiry_date']
    search_fields = ['passport_number', 'client__first_name', 'client__last_name']

@admin.register(PotentialClient)
class PotentialClientAdmin(admin.ModelAdmin):
    list_display = ['client_id', 'phone', 'contract_id']
    search_fields = ['client_id', 'phone', 'contract_id']

@admin.register(TelegramUser)
class TelegramUserAdmin(admin.ModelAdmin):
    list_display = ['telegram_id', 'first_name', 'last_name', 'phone_number', 'username', 'approved']
    search_fields = ['telegram_id', 'first_name', 'last_name', 'phone_number', 'username']

@admin.register(TelegramUserLog)
class TelegramUserLogAdmin(admin.ModelAdmin):
    list_display = ['user', 'action', 'timestamp']
    search_fields = ['user__telegram_id', 'action']

