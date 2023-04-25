from bot.models import Account, BotTgGroup
from asgiref.sync import sync_to_async

@sync_to_async
def is_authenticated(telegram_id):
    user = Account.objects.filter(telegramId=telegram_id).exists()

    if user:
        return True
    
    return False


@sync_to_async
def create_user(data):
    telegramId = data.get("telegramId")
    firstName = data.get("firstName")
    lastName = data.get("lastName")
    username = data.get("username")
    language = data.get("language")
    phoneNumber = data.get("phoneNumber")

    user = Account.objects.create(telegramId=telegramId, firstName=firstName, lastName=lastName, username=username, language=language, phoneNumber=phoneNumber)
    
    return user
    
@sync_to_async
def user_me(telegram_id):
    user = Account.objects.get(telegramId=telegram_id)
    
    return user



@sync_to_async
def get_botgroup():
    group = BotTgGroup.objects.first()
    
    return group.telegramId



@sync_to_async
def get_user_language(telegram_id):
    user = Account.objects.get(telegramId=telegram_id)

    return user.language


@sync_to_async
def update_user(firstName, lastName, telegramId):
    user = Account.objects.get(telegramId=telegramId)
    user.firstName = firstName
    user.lastName = lastName

    user.save()

    return user


@sync_to_async
def set_language(telegram_id, lang):
    user = Account.objects.get(telegramId=telegram_id)
    user.language = lang
    user.save()