from aiogram import F, Router
from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery
from loguru import logger

from handlers.message_handler import cmd_start
from tracker_client import get_client
from config import config
from state.repair_state import RepairState, ServiceState
from keybords.inline_keyboard import back_to_menu_button

callback_router = Router()
tracker_client = get_client.get_tracker_client(config.tracker_token, config.tracker_org_id)


@callback_router.callback_query(F.data == 'back_to_menu')
async def cmd_repair(callback: CallbackQuery, state: FSMContext):
    await state.clear()
    await cmd_start(callback.message)


@callback_router.callback_query(F.data == 'repair')
async def cmd_repair(callback: CallbackQuery, state: FSMContext):
    await state.update_data(state='ремонт')
    await state.set_state(RepairState.auto_model)
    await callback.message.edit_text(f"Укажите модель авто", reply_markup=back_to_menu_button)


@callback_router.callback_query(F.data == 'send_task')
async def cmd_repair(callback: CallbackQuery, state: FSMContext):
    data = await state.get_data()
    res = tracker_client.issues.create(
        queue='TESTVAGBOARD', summary=f"{data['state']} {data['auto_model']}",
        description=
        f"Тип обращения: {data['state']}\n"
        f"Марка авто: {data['auto_model']}\n"
        f"Текст обращения: {data['user_text']}\n"
        f"Контакт для связи: {data['phone_number']}\n"
    )
    await state.clear()
    await callback.message.answer(f"Заявка отправлена id заявки {res.key}")
    logger.info(f'Task {res.key} created')


@callback_router.callback_query(F.data == 'technical_service')
async def cmd_technical_service(callback: CallbackQuery, state: FSMContext):
    await state.update_data(state='то')
    await state.set_state(ServiceState.auto_model)
    await callback.message.edit_text(f"Укажите модель авто", reply_markup=back_to_menu_button)
