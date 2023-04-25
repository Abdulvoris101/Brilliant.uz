from django.conf import settings
import requests

class BotConfig:
    def __init__(self, to):
        self.token = settings.TOKEN_BOT
        self.accounts = to
        self.url = f"https://api.telegram.org/bot{self.token}"
    
    def getMe(self):
        self.user = requests.get(f"{self.url}/getMe").json()

    def getChats(self):
        chats = [account.telegramId for account in self.accounts]

        return chats
        
    def __str__(self):
        return str(self.user)

class SendMethod(BotConfig):
    def __init__(self, to, method, arg, value, chatId=None):
        super().__init__(to)
        self.method = method
        self.chatId = chatId
        self.arg = arg
        self.value = value
    
    def sendToAll(self):
        for chatId in self.getChats():
            requests.get(f"{self.url}/{self.method}?chat_id={chatId}&{self.arg}={self.value}").json()
    
    def send(self):
        requests.get(f"{self.url}/{self.method}?chat_id={self.chatId}&{self.arg}={self.value}").json()


class SendSticker(SendMethod):
    def __init__(self, stickerId, to):
        super().__init__(to, method="sendSticker", arg="sticker", value=stickerId)
        self.sendToAll()
    


class SendMessage(SendMethod):
    def __init__(self, message, to):
        super().__init__(to, method="sendMessage", arg="text", value=message)
        self.message = message
        self.sendToAll()
    

    


