from .run import types
from bot.management.commands.manager import user_me
from .utils import translate_text


async def settings_keyboard(lang, user_id):
    user = await user_me(user_id)
    
    settings_keyboard_ = types.ReplyKeyboardMarkup([
        [
            types.KeyboardButton(translate_text(f"Tilni o'zgartirish", lang) + f"({lang})"),
            types.KeyboardButton(translate_text("Ismni o'zgartirish", lang) + f"({user.firstName})")
        ],
        [
            types.KeyboardButton(translate_text("Familiyani o'zgartirish", lang)  + f"({user.lastName})")
        ]
    ], resize_keyboard=True, one_time_keyboard=True
    )

    settings_keyboard_.add(translate_text("⬅️ Orqaga", lang))

    return settings_keyboard_
    

language_keyboards = types.ReplyKeyboardMarkup([
    [
        types.KeyboardButton("uz"),
        types.KeyboardButton("ru")
    ]

],resize_keyboard=True)

def start_keyboards(lang):
    
    start_keyboards = types.ReplyKeyboardMarkup([
        [
            types.KeyboardButton(f'🚀 {translate_text(text="Buyurtma", lang=lang)}'),
        ],
        [

            types.KeyboardButton(f'💬 {translate_text(text="Murojat", lang=lang)}'),
            types.KeyboardButton(f'⚙️ {translate_text(text="Sozlamalar", lang=lang)}'),
        ],
        [
            types.KeyboardButton(f'⚡️ {translate_text(text="Ijtimoiy tarmoqlar", lang=lang)}'),
        ]

    ],resize_keyboard=True, one_time_keyboard=True)

    return start_keyboards


def get_location_keyboards(lang):
    text = "📌 Lokatsiyani yuborish"
    location_keyboards = types.ReplyKeyboardMarkup([
        [
            types.KeyboardButton(text=translate_text(text, lang), request_location=True),
        ],
        [
            types.KeyboardButton(text=translate_text("⬅️ Orqaga", lang)),
        ]
    ], resize_keyboard=True, one_time_keyboard=True)

    return location_keyboards



def contact_keyboards(lang):
    text = "Raqamni yuborish"
    contact_keyboards = types.ReplyKeyboardMarkup([
        [
            types.KeyboardButton(text=translate_text(text, lang), request_contact=True)
        ]
    ], resize_keyboard=True, one_time_keyboard=True)

    return contact_keyboards

cancel_keyboards = types.ReplyKeyboardMarkup(resize_keyboard=True).add("/cancel")

