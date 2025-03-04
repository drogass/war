from aiogram import types
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

military_ranks = {
    "Рядовой": "Рядовой — базовое звание. Основные обязанности: выполнение приказов командира и выполнение общих задач подразделения.",
    "Ефрейтор": "Ефрейтор — звание выше рядового. Основные обязанности аналогичны обязанностям рядового, но может командовать небольшим числом военнослужащих.",
    "Младший сержант": "Младший сержант — помощник командира отделения. Обязанности: руководство малым подразделением и выполнение задач, поставленных командиром.",
    "Сержант": "Сержант — командир отделения. Основные обязанности: управление отделением, обучение личного состава.",
    "Старший сержант": "Старший сержант — старший командир отделения. Обязанности: управление отделением и контроль выполнения задач.",
    "Старшина": "Старшина — старший унтер-офицер, ответственный за дисциплину и порядок в подразделении. Обязанности: административное руководство и помощь командирам.",
    "Прапорщик": "Прапорщик — звание младшего офицера. Основные обязанности: выполнение задач, поставленных командованием, и управление небольшими подразделениями.",
    "Старший прапорщик": "Старший прапорщик — старший унтер-офицер. Обязанности: руководство и контроль за выполнением задач в подчиненных подразделениях.",
    "Младший лейтенант": "Младший лейтенант — младший офицер. Основные обязанности: выполнение командных функций и управление взводом.",
    "Лейтенант": "Лейтенант — командир взвода. Основные обязанности: планирование и руководство действиями взвода.",
    "Старший лейтенант": "Старший лейтенант — старший командир взвода. Обязанности: управление взводом и выполнение задач, поставленных командованием.",
    "Капитан": "Капитан — командир роты. Основные обязанности: управление ротой, координация действий взводов.",
    "Майор": "Майор — старший офицер. Основные обязанности: выполнение задач на уровне батальона и выше.",
    "Подполковник": "Подполковник — заместитель командира полка. Обязанности: помощь командиру полка и выполнение командных функций.",
    "Полковник": "Полковник — командир полка. Основные обязанности: управление полком и координация боевых операций.",
    "Генерал-майор": "Генерал-майор — младший генеральский ранг. Основные обязанности: стратегическое планирование и руководство крупными соединениями.",
    "Генерал-лейтенант": "Генерал-лейтенант — средний генеральский ранг. Основные обязанности: руководство армейскими корпусами и выполнение стратегических задач.",
    "Генерал-полковник": "Генерал-полковник — старший генеральский ранг. Основные обязанности: стратегическое руководство вооруженными силами на уровне фронта.",
    "Генерал армии": "Генерал армии — высший офицерский ранг. Основные обязанности: высшее стратегическое руководство вооруженными силами."
}

def create_inline_keyboard():
    keyboard = InlineKeyboardMarkup()
    for item in military_ranks.keys():
        keyboard.add(InlineKeyboardButton(item, callback_data=item))
    return keyboard

def register_ranks_handlers(dp):
    @dp.message_handler(lambda message: message.text == "Показать военные звания")
    async def show_ranks(message: types.Message):
        keyboard = create_inline_keyboard()
        await message.answer("Выберите звание из списка:", reply_markup=keyboard)

    @dp.callback_query_handler(lambda c: c.data in military_ranks.keys())
    async def send_rank_info(callback_query: types.CallbackQuery):
        rank_name = callback_query.data
        rank_info = military_ranks[rank_name]
        await dp.bot.answer_callback_query(callback_query.id)  # Подтверждение обработки callback query
        await dp.bot.send_message(callback_query.from_user.id, f"{rank_name}:\n{rank_info}")
