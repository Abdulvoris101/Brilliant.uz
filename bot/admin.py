from django.contrib import admin
from .models import Account, Message, Sticker, BotTgGroup

admin.site.register(Message)
admin.site.register(Sticker)
admin.site.register(BotTgGroup)


@admin.register(Account)
class AccountAdmin(admin.ModelAdmin):
    list_display = ("telegramId", "firstName", "username", "phoneNumber")
    list_display_links = ("telegramId", "firstName", "username")
    readonly_fields = ("telegramId", "username", "phoneNumber")
