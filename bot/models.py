from django.db import models
from .api import SendMessage, SendSticker


class Account(models.Model):
    telegramId = models.BigIntegerField()
    firstName = models.CharField(max_length=255)
    lastName = models.CharField(max_length=255, null=True, blank=True)
    username = models.CharField(max_length=255, null=True, blank=True)
    phoneNumber = models.BigIntegerField()
    language = models.CharField(max_length=255)

    def __str__(self):
        return self.firstName


class BotTgGroup(models.Model):
    telegramId = models.CharField(max_length=500, default='-1001875684284')

    class Meta:
        verbose_name = "Telegram Group Id"
        verbose_name_plural = "Telegram Group Id"
    
    def __str__(self):
        return str(self.telegramId)

class Sticker(models.Model):
    stickerId = models.TextField()


    def save(self, *args, **kwargs):

        if not self.pk:
            SendSticker(stickerId=self.stickerId, to=Account.objects.all())

        super().save(*args, **kwargs)

    def __str__(self):
        return f"Sticker-{self.id}"

class Message(models.Model):
    message = models.TextField()

    def save(self, *args, **kwargs):

        if not self.pk:
            SendMessage(message=self.message, to=Account.objects.all())

        super().save(*args, **kwargs)

    def __str__(self):
        return self.message


