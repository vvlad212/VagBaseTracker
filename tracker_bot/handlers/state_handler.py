from aiogram import F, Router
from aiogram.fsm.context import FSMContext
from aiogram.types import Message

from handlers.callback_handler import tracker_client
from keybords.inline_keyboard import send_task_button
from state.repair_state import RepairState, UserState,ServiceState

state_router = Router()

# Repair
@state_router.message(RepairState.auto_model)
async def cmd_repair_text(message: Message, state: FSMContext):
    await state.update_data(auto_model=message.text)
    await state.set_state(RepairState.user_text)
    await message.answer(f"Опишите проблему")


@state_router.message(RepairState.user_text)
async def cmd_phone_number(message: Message, state: FSMContext):
    await state.update_data(user_text=message.text)
    await state.set_state(RepairState.phone_number)
    await message.answer(f"Как с вами связаться? (телефон/ссылка на телеграм)")


@state_router.message(UserState.phone_number)
async def cmd_phone_number(message: Message, state: FSMContext):
    await state.update_data(phone_number=message.text)
    await state.set_state(RepairState.phone_number)

    data = await state.get_data()
    await message.answer(f"Итак, ваша заявка\n"
                            f"Марка авто: {data['auto_model']}\n"
                            f"Текст обращения: {data['user_text']}\n"
                            f"Контакт для связи: {data['phone_number']}\n\n"
                            f"все верно?",reply_markup=send_task_button
                            )