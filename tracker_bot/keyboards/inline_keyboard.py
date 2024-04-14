from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

sign_up_keyboard = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Ремонт', callback_data='repair')],
    [InlineKeyboardButton(text='ТО', callback_data='technical_service')],
]
)

send_task_button = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Да, все верно', callback_data='send_task')]
]
)

back_to_menu_button = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Назад в меню', callback_data='back_to_menu')]
]
)

