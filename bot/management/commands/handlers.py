from .run import dp, bot, types, UpdateUserState, ClientStateGroup, MessageState
from .keyboards import start_keyboards, language_keyboards,  get_location_keyboards, contact_keyboards, settings_keyboard
from bot.management.commands.manager import is_authenticated, get_botgroup, user_me, get_user_language, set_language, create_user, update_user
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher.storage import FSMContext
from .utils import send_message_local
from aiogram.dispatcher.filters import Text


@dp.message_handler(commands=['cancel'], state="*")
async def cancel_register(message: types.Message, state: FSMContext):
    current_state = await state.get_state()
    
    if current_state is None:
        return 

    
    async with state.proxy() as data:
        
        await send_message_local(message.from_user.id, text="Ro'yhatdan o'tish bekor qilindi! /start", lang=data['language'])

    await state.finish()



@dp.message_handler(lambda message: message.text, state=ClientStateGroup.language)
async def receiver_language(message: types.Message, state: FSMContext):
    
    async with state.proxy() as data:
        data['language'] = message.text
    
    await ClientStateGroup.next()

    await send_message_local(user_id=message.from_user.id,
    text="Telefon raqamingizni jo'nating. <b>Raqamni yuborish </b>  tugmasini bosing", lang=message.text, reply_markup=contact_keyboards(lang=message.text))


@dp.message_handler(lambda message: message.text != 'ru' or message.text != 'uz', state=ClientStateGroup.language)
async def incorrect_language(message: types.Message, state=FSMContext):
    await message.answer("Iltimos to'g'ri tilni tanlang. Пожалуйста введите коректный язык")
    

@dp.message_handler(lambda message: message.contact.phone_number, content_types=['contact'], state=ClientStateGroup.phone_number)
async def handle_contact(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        
        data['phone_number'] = message.contact.phone_number
        lang = data['language']
        
        if message.contact.phone_number[0] == '+':
            if str(data['phone_number'])[:4] != '+998':
                return await send_message_local(message.from_user.id, text=f"Siz faqatgina O'zbekiston nomer orqali tizimga kira olasiz", lang=lang)
            
            await send_message_local(message.from_user.id, text=f"Ro'yhatdan muvaffiqiyatli o'tdingiz {message.from_user.first_name} 🤴", lang=lang, reply_markup=start_keyboards(lang))
        else:
            if str(data['phone_number'])[:3] != '998':
                return await send_message_local(message.from_user.id, text=f"Siz faqatgina O'zbekiston nomer orqali tizimga kira olasiz", lang=lang)
            
            await send_message_local(message.from_user.id, text=f"Ro'yhatdan muvaffiqiyatli o'tdingiz {message.from_user.first_name} 🤴", lang=lang, reply_markup=start_keyboards(lang))


        if str(data['phone_number'])[0] == '+':
            phone_number = str(data['phone_number']).replace('+998', '')
        else:
            phone_number = str(data['phone_number']).replace('998', '')
        
        
        data = {
            "phoneNumber":  phone_number,
            "firstName": message.from_user.first_name,
            "lastName": message.from_user.last_name if message.from_user.last_name is not None else 'null',
            "telegramId": message.from_user.id,
            "username": message.from_user.username if message.from_user.username is not None else 'null',
            "language": lang
        }
        
        user = await create_user(data=data)


    await state.finish()





# Work on it 

# Settings




@dp.message_handler(Text(equals=["⚙️ Настройки", "⚙️ Sozlamalar"]))
async def settings_view(message: types.Message):
    language = await get_user_language(message.from_user.id)
    await send_message_local(message.from_user.id, "⚙️ Sozlamalar", lang=language, reply_markup=await settings_keyboard(language, message.from_user.id))




@dp.message_handler(Text(equals=["Изменить язык(ru)", "Tilni o'zgartirish(uz)"]))
async def set_lang(message: types.Message):
    language = await get_user_language(message.from_user.id)

    if language == "ru":
        await set_language(message.from_user.id, "uz")
    else:
        await set_language(message.from_user.id, "ru")

    language = await get_user_language(message.from_user.id)
    
    await settings_view(message)
    

# Social Media

# Ijtimoiy tarmoqlar

@dp.message_handler(Text(equals=["⚡️ Ijtimoiy tarmoqlar", "⚡️ Социальные сети"]))
async def chat(message: types.Message):
    language = await get_user_language(message.from_user.id)

    await bot.delete_message(message.from_user.id, message.message_id)

    await bot.send_message( message.from_user.id, "<a href='https://www.instagram.com/Jalyuziuzbekistan/'>Instagram</a>\n<a href='https://t.me/brilliantuzbekistan'>Telegram</a>", reply_markup=start_keyboards(lang=language))

# C0hat
@dp.message_handler(Text(equals=["💬 Murojat", "💬 Обращаться"]))
async def chat(message: types.Message, state=None):
    language = await get_user_language(message.from_user.id)
    await bot.delete_message(message.from_user.id, message.message_id)

    await MessageState.message.set()

    await send_message_local(message.from_user.id, "Xabar yuboring", language)

@dp.message_handler(state=MessageState.message)
async def message_handle(message: types.Message, state=FSMContext):
    language = await get_user_language(message.from_user.id)
    me = await user_me(telegram_id=message.from_user.id)
    group_id = await get_botgroup()

    msg = f"От: Brilliant\ntelegramId: <code>{message.from_user.id}</code>\nИмя: {message.from_user.first_name}\nUsername: @{message.from_user.username}\nТип: Сообщения\nТел.номер:{me.phoneNumber}\nСообшения: {message.text}"

    await bot.send_message(group_id, msg)

    await state.finish()

    await send_message_local(message.from_user.id, "Xabaringiz muvaffiqiyatli yuborildi. Tez orada administratorlar sizga javob berishadi 😊", language, reply_markup=start_keyboards(lang=language))
    


@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message, state=None):   

    if await is_authenticated(message.from_user.id) == True:
        language = await  get_user_language(message.from_user.id)

        return await send_message_local(message.from_user.id, text=f"Assalomu aleykum <b>{message.from_user.first_name}</b> 😊\n\nNima buyurtma qilamiz ?", lang=language, reply_markup=start_keyboards(lang=language))
    
    await ClientStateGroup.language.set()

    await bot.send_message(chat_id=message.from_user.id, text=f"""
        Assalomu Alaykum! Bizning botdan foydalanish uchun ro'yxatdan o'ting\n\nЗдравствуйте! Чтобы пользоваться нашим ботом вам необходимо пройти регистрацию.
    """)

    await bot.send_message(chat_id=message.from_user.id, text=f"""
        Tilingizni tanlang\n\nВыберите ваш язык
    """, reply_markup=language_keyboards)





# Functions



# Address



@dp.message_handler(content_types=['location'])
async def get_location(message: types.Location):
    me = await  user_me(telegram_id=message.from_user.id)
    msg = f"telegramId: <code>{message.from_user.id}</code>\nИмя: {message.from_user.first_name}\nUsername: @{message.from_user.username}\nТип: Быстрый заказ\nТел.номер:{me.phoneNumber}\nЛокация: {message.location.latitude}, {message.location.longitude}"

    await bot.send_message("", msg)


    await bot.send_message(message.from_user.id, "Buyurtma qabul qilindi tez orada siz bilan bog'lanamiz")


@dp.message_handler(Text(equals=["🚀 Buyurtma", "🚀 Заказ"], ignore_case=True))
async def to_shop(message: types.Message):
    language = await get_user_language(message.from_user.id)

    await send_message_local(message.from_user.id, "Lokatsiyani yuboring", lang=language, reply_markup=get_location_keyboards(lang=language))

    


@dp.message_handler(Text(equals=["⬅️ Назад", "⬅️ Orqaga"], ignore_case=True))
async def to_start(message: types.Message):
    await send_welcome(message)




@dp.message_handler()
async def handle_message(message: types.Message, state=None):
    language  = await get_user_language(message.from_user.id)
    user = await user_me(telegram_id=message.from_user.id)

    if message.text == f"Изменение имени({user.firstName})" or message.text == f"Ismni o'zgartirish({user.firstName})":
        
        await UpdateUserState.first_name.set()
        await send_message_local(message.from_user.id, "Yangi ism kiriting: ", language)

    elif message.text == f"Смена фамилии({user.lastName})" or message.text == f"Familiyani o'zgartirish({user.lastName})":
        await UpdateUserState.last_name.set()
        await send_message_local(message.from_user.id, "Yangi familiya kiriting: ", language)





@dp.message_handler(state=UpdateUserState.first_name)
async def first_name(message: types.Message, state=FSMContext):
    lang = await get_user_language(message.from_user.id)
    user = await user_me(message.from_user.id)

    async with state.proxy() as data:
        data['first_name'] = message.text
        data['last_name'] = "message.text"

    await update_user(firstName=message.text, lastName=user.lastName, telegramId=message.from_user.id)
    
    await state.finish()
    await send_message_local(message.from_user.id, "Ism o'zgardi", lang)
    await send_welcome(message)


@dp.message_handler(state=UpdateUserState.last_name)
async def last_name(message: types.Message, state=FSMContext):
    lang = await get_user_language(message.from_user.id)
    user = await user_me(message.from_user.id)

    await update_user(firstName=user.firstName, lastName=message.text, telegramId=message.from_user.id)


    await state.finish()
    await send_message_local(message.from_user.id, "Familiya o'zgardi", lang)
    await send_welcome(message)



