from aiogram  import types, Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text, state
from aiogram.dispatcher.filters.state import State, StatesGroup


class FSM_reg(StatesGroup):
    model = State()
    size = State()
    category = State()
    price = State()
    photo = State()
    submit = State()
    productid = State()
    infoproductid = State()


async def start_fsm_regi(message: types.Message):
    await FSM_reg.model.set()
    await message.answer('Введите модель обуви:')


async def load_model(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['model'] = message.text


    await FSM_reg.next()
    await message.answer('Укажите размер обуви:')


async def load_size(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['size'] = message.text


    await FSM_reg.next()
    await message.answer('Укажите категорию:')

async def load_category(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['category'] = message.text

    await FSM_reg.next()
    await message.answer('Укажите стоимость:')

async def load_price(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['price'] = message.text


    await FSM_reg.next()
    await message.answer('Отправьте фото:')

async def load_photo(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['photo'] = message.photo[-1].file_id

    await FSM_reg.next()
    await message.answer('Верны ли данные о товаре?:')
    await message.answer_photo(photo=data['photo'],
                               caption=f'model - {data["model"]}\n'
                                       f'size - {data["size"]}\n'
                                       f'category - {data["category"]}\n'
                                       f'price - {data["price"]}\n' )


async def submit(message: types.Message, state: FSMContext):
    if message.text== 'да':
        async with state.proxy() as data:
            await message.answer('товар базе!')

        await state.finish()

    elif message.text == 'нет':
        await message.answer('Отменено!')
        await state.finish()

    else:
         await message.answer('Выберите да или нет?')


def register_handlers_fsm(dp: Dispatcher):
    dp.register_message_handler(start_fsm_regi, commands=['regis'])
    dp.register_message_handler(load_model,state=FSM_reg.model)
    dp.register_message_handler(load_size,state=FSM_reg.size)
    dp.register_message_handler(load_category,state=FSM_reg.category)
    dp.register_message_handler(load_price,state=FSM_reg.price)
    dp.register_message_handler(load_photo,state=FSM_reg.photo, content_types=['photo'])
    dp.register_message_handler(submit,state=FSM_reg.submit)



