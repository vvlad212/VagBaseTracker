from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

menu_keyboard = ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text='Записаться')],
                                              # [KeyboardButton(text='Отменить запись')],
                                              # [KeyboardButton(text='Узнать статус')],
                                              ],
                                    resize_keyboard=True,
                                    input_field_placeholder="Выберете действие",
                                    one_time_keyboard=True
                                    )
