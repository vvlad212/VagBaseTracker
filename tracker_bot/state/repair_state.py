from aiogram.fsm.state import State, StatesGroup


class UserState(StatesGroup):
    phone_number = State()


class RepairState(UserState):
    state = State()
    auto_model = State()
    user_text = State()


class ServiceState(UserState):
    state = State()
    auto_model = State()
    user_text = State()
