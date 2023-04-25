from django.core.management.base import BaseCommand
from aiogram import Bot, Dispatcher, types, executor
from aiogram.dispatcher.filters.state import StatesGroup, State
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from django.conf import settings


storage = MemoryStorage()



bot = Bot(token=settings.TOKEN_BOT, parse_mode='HTML')
dp = Dispatcher(bot, storage=storage)


class ClientStateGroup(StatesGroup):
    language = State()
    phone_number = State()

class ProductEditState(StatesGroup):
    product_id = State()
    square = State()

class AddressStateGroup(StatesGroup):
    city = State()
    district = State()
    house = State()

class MessageState(StatesGroup):
    message = State()


class UpdateUserState(StatesGroup):
    first_name = State()
    last_name = State()

class Command(BaseCommand):
    help = 'Telegram-bot'

    def handle(self, *args, **options):
        from .handlers import dp

        executor.start_polling(dp, skip_updates=True)