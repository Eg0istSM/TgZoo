import telebot
from config import TOKEN
from telebot import types
from animals import animals

bot = telebot.TeleBot(TOKEN)


# приветствие и первая информация
@bot.message_handler(commands=['start', 'help'])
def start(message: telebot.types.Message):
    first_name = message.chat.first_name
    bot.send_message(message.chat.id, f"Здравствуйте {first_name}\n"
                                      f"Чтобы узнать ваше тотемное животное введите /quiz\n"
                                      f"Для помощи введите /help \nДополнительная информация /info")


# вход в викторину
@bot.message_handler(commands=['quiz'])
def open_quiz(message):
    kb = types.InlineKeyboardMarkup(row_width=1)
    btn1 = types.InlineKeyboardButton(text='ДА', callback_data='yes')
    btn2 = types.InlineKeyboardButton(text='НЕТ', callback_data='no')
    kb.add(btn1, btn2)
    bot.send_message(message.chat.id,
                     'Чтобы узнать ваше тотемное животное нужно пройти викторину,вы хотите пройти викторину сейчас?',
                     reply_markup=kb)


@bot.callback_query_handler(func=lambda call: call.data == 'yes')
def question(call: types.CallbackQuery):
    kb = types.InlineKeyboardMarkup(row_width=1)
    btn1 = types.InlineKeyboardButton(text='Футбол', callback_data='football')
    btn2 = types.InlineKeyboardButton(text='Хоккей', callback_data='hockey')
    btn3 = types.InlineKeyboardButton(text='Тенис', callback_data='tenis')
    kb.add(btn1, btn2, btn3)
    bot.send_message(call.message.chat.id,
                     'Какой вид спорта вы выберете?',
                     reply_markup=kb)


@bot.callback_query_handler(func=lambda call: call.data == 'football')
def question_2(call: types.CallbackQuery):
    kb = types.InlineKeyboardMarkup(row_width=1)
    btn1 = types.InlineKeyboardButton(text='Легкий овощной салат', callback_data='herbivores')
    btn2 = types.InlineKeyboardButton(text='Стейк с кровью', callback_data='predator')
    kb.add(btn1, btn2, )
    bot.send_message(call.message.chat.id,
                     'Какое блюдо вы выберете?',
                     reply_markup=kb)


@bot.callback_query_handler(func=lambda call: call.data == 'predator')
def question_3(call: types.CallbackQuery):
    kb = types.InlineKeyboardMarkup(row_width=1)
    btn1 = types.InlineKeyboardButton(text='Прогулка в лесу', callback_data='forest')
    btn2 = types.InlineKeyboardButton(text='Поваляться на песочке', callback_data='desert')
    kb.add(btn1, btn2, )
    bot.send_message(call.message.chat.id,
                     'Какой отдых вы выбрали бы?',
                     reply_markup=kb)


@bot.callback_query_handler(func=lambda call: call.data == 'forest')
def question_4(call: types.CallbackQuery):
    kb = types.InlineKeyboardMarkup(row_width=1)
    btn1 = types.InlineKeyboardButton(text='Рюриковичи мы!', callback_data='indian_lion')
    btn2 = types.InlineKeyboardButton(text='Нет нету', callback_data='the_marten')
    kb.add(btn1, btn2, )
    bot.send_message(call.message.chat.id,
                     'Есть ли у вас царские корни?',
                     reply_markup=kb)


@bot.callback_query_handler(func=lambda call: call.data == 'desert')
def question_5(call: types.CallbackQuery):
    kb = types.InlineKeyboardMarkup(row_width=1)
    btn1 = types.InlineKeyboardButton(text='Вечер с друзьями', callback_data='The_jackal')
    btn2 = types.InlineKeyboardButton(text='Чтение книги', callback_data='manul')
    kb.add(btn1, btn2, )
    bot.send_message(call.message.chat.id,
                     'Какой досуг вы предпоитаете?',
                     reply_markup=kb)


@bot.callback_query_handler(func=lambda call: call.data == 'herbivores')
def question_6(call: types.CallbackQuery):
    kb = types.InlineKeyboardMarkup(row_width=1)
    btn1 = types.InlineKeyboardButton(text='Тропический лес', callback_data='tropik')
    btn2 = types.InlineKeyboardButton(text='Тихая саванна', callback_data='savanna')
    kb.add(btn1, btn2, )
    bot.send_message(call.message.chat.id,
                     'Какая природа вам по душе? ',
                     reply_markup=kb)


@bot.callback_query_handler(func=lambda call: call.data == 'tropik')
def question_7(call: types.CallbackQuery):
    kb = types.InlineKeyboardMarkup(row_width=1)
    btn1 = types.InlineKeyboardButton(text='люблю потрещать языком', callback_data='capybara')
    btn2 = types.InlineKeyboardButton(text='Предпочитаю слушать', callback_data='tamarin')
    kb.add(btn1, btn2, )
    bot.send_message(call.message.chat.id,
                     'Как вы ведете себя в беседе?',
                     reply_markup=kb)


@bot.callback_query_handler(func=lambda call: call.data == 'savanna')
def question_8(call: types.CallbackQuery):
    kb = types.InlineKeyboardMarkup(row_width=1)
    btn1 = types.InlineKeyboardButton(text='Да, я шпала', callback_data='giraffe')
    btn2 = types.InlineKeyboardButton(text='Нет,я гном', callback_data='dicdic')
    kb.add(btn1, btn2, )
    bot.send_message(call.message.chat.id,
                     'Высокий ли у вас рост?',
                     reply_markup=kb)


@bot.callback_query_handler(func=lambda call: call.data == 'hockey')
def question_9(call: types.CallbackQuery):
    kb = types.InlineKeyboardMarkup(row_width=1)
    btn1 = types.InlineKeyboardButton(text='Легкий овощной салат', callback_data='winter herbivores')
    btn2 = types.InlineKeyboardButton(text='Стейк с кровью', callback_data='winter predator')
    kb.add(btn1, btn2, )
    bot.send_message(call.message.chat.id,
                     'Какое блюдо вы выберете?',
                     reply_markup=kb)


@bot.callback_query_handler(func=lambda call: call.data == 'winter predator')
def question_10(call: types.CallbackQuery):
    kb = types.InlineKeyboardMarkup(row_width=1)
    btn1 = types.InlineKeyboardButton(text='Ветренные холмы', callback_data='hill')
    btn2 = types.InlineKeyboardButton(text='Снежные степи', callback_data='snowy steppes')
    kb.add(btn1, btn2, )
    bot.send_message(call.message.chat.id,
                     'Какая природа вам по душе?',
                     reply_markup=kb)


@bot.callback_query_handler(func=lambda call: call.data == 'winter herbivores')
def question_11(call: types.CallbackQuery):
    kb = types.InlineKeyboardMarkup(row_width=1)
    btn1 = types.InlineKeyboardButton(text='Плывущие льдины', callback_data='winter aqua')
    btn2 = types.InlineKeyboardButton(text='Снежные степи', callback_data='herb snowy steppes')
    kb.add(btn1, btn2, )
    bot.send_message(call.message.chat.id,
                     'Какая природа вам по душе?',
                     reply_markup=kb)


@bot.callback_query_handler(func=lambda call: call.data == 'hill')
def question_12(call: types.CallbackQuery):
    kb = types.InlineKeyboardMarkup(row_width=1)
    btn1 = types.InlineKeyboardButton(text='Собак', callback_data='The scribe')
    btn2 = types.InlineKeyboardButton(text='Кошек', callback_data='lynx')
    kb.add(btn1, btn2, )
    bot.send_message(call.message.chat.id,
                     'Какких домашних животных вы предпочитаете?',
                     reply_markup=kb)


@bot.callback_query_handler(func=lambda call: call.data == 'snowy steppes')
def question_13(call: types.CallbackQuery):
    kb = types.InlineKeyboardMarkup(row_width=1)
    btn1 = types.InlineKeyboardButton(text='Охота', callback_data='manul_s')
    btn2 = types.InlineKeyboardButton(text='Рыбалка', callback_data='polar bear')
    kb.add(btn1, btn2, )
    bot.send_message(call.message.chat.id,
                     'Какак досуг вы предпочитаете?',
                     reply_markup=kb)


@bot.callback_query_handler(func=lambda call: call.data == 'winter aqua')
def question_14(call: types.CallbackQuery):
    kb = types.InlineKeyboardMarkup(row_width=1)
    btn1 = types.InlineKeyboardButton(text='Конечно пойдут', callback_data='walrus')
    btn2 = types.InlineKeyboardButton(text='Нет, не пойдут', callback_data='larga')
    kb.add(btn1, btn2, )
    bot.send_message(call.message.chat.id,
                     'Пойдут ли вам усы?',
                     reply_markup=kb)


@bot.callback_query_handler(func=lambda call: call.data == 'herb snowy steppes')
def question_15(call: types.CallbackQuery):
    kb = types.InlineKeyboardMarkup(row_width=1)
    btn1 = types.InlineKeyboardButton(text='нет ,не люблю', callback_data='The blue ram')
    btn2 = types.InlineKeyboardButton(text='Обожаю плескаться в водичке', callback_data='navy seal')
    kb.add(btn1, btn2, )
    bot.send_message(call.message.chat.id,
                     'Любите ли вы плавать?',
                     reply_markup=kb)


@bot.callback_query_handler(func=lambda call: call.data == 'tenis')
def question_16(call: types.CallbackQuery):
    kb = types.InlineKeyboardMarkup(row_width=1)
    btn1 = types.InlineKeyboardButton(text='сноуборд,лыжи,снегоход', callback_data='fly winter')
    btn2 = types.InlineKeyboardButton(text='катамаран,велосипед', callback_data='fly warm')
    kb.add(btn1, btn2, )
    bot.send_message(call.message.chat.id,
                     'Какой отдых вы предпочтете?',
                     reply_markup=kb)


@bot.callback_query_handler(func=lambda call: call.data == 'fly winter')
def question_17(call: types.CallbackQuery):
    kb = types.InlineKeyboardMarkup(row_width=1)
    btn1 = types.InlineKeyboardButton(text='Суши с рыбой и икрой', callback_data='fly Eating fish')
    btn2 = types.InlineKeyboardButton(text='Английский завтрак', callback_data='fly predator')
    kb.add(btn1, btn2, )
    bot.send_message(call.message.chat.id,
                     'Какое блюдо вы выберете на завтрак?',
                     reply_markup=kb)


@bot.callback_query_handler(func=lambda call: call.data == 'fly predator')
def question_18(call: types.CallbackQuery):
    kb = types.InlineKeyboardMarkup(row_width=1)
    btn1 = types.InlineKeyboardButton(text='Самолет', callback_data='Snowy owl')
    btn2 = types.InlineKeyboardButton(text='Любой вид транспорта', callback_data='Mallard')
    kb.add(btn1, btn2, )
    bot.send_message(call.message.chat.id,
                     'На какой транспорте предпочитаете добираться на отдых?',
                     reply_markup=kb)


@bot.callback_query_handler(func=lambda call: call.data == 'fly Eating fish')
def question_19(call: types.CallbackQuery):
    kb = types.InlineKeyboardMarkup(row_width=1)
    btn1 = types.InlineKeyboardButton(text='Нееет', callback_data='Jackass penguin')
    btn2 = types.InlineKeyboardButton(text='О да', callback_data='Gentoo penguin')
    kb.add(btn1, btn2, )
    bot.send_message(call.message.chat.id,
                     'Любите ли вы быструю скорость?',
                     reply_markup=kb)


@bot.callback_query_handler(func=lambda call: call.data == 'fly warm')
def question_20(call: types.CallbackQuery):
    kb = types.InlineKeyboardMarkup(row_width=1)
    btn1 = types.InlineKeyboardButton(text='Стейк', callback_data='fly warm predator')
    btn2 = types.InlineKeyboardButton(text='Фрукторый салат', callback_data='fly frugivores')
    kb.add(btn1, btn2, )
    bot.send_message(call.message.chat.id,
                     'Какое блюдо выберете?',
                     reply_markup=kb)


@bot.callback_query_handler(func=lambda call: call.data == 'fly warm predator')
def question_21(call: types.CallbackQuery):
    kb = types.InlineKeyboardMarkup(row_width=1)
    btn1 = types.InlineKeyboardButton(text='День', callback_data='Lesser spotted eagle')
    btn2 = types.InlineKeyboardButton(text='Ночь', callback_data='Long-eared owl')
    kb.add(btn1, btn2, )
    bot.send_message(call.message.chat.id,
                     'В какое время суток вы бодорствуете?',
                     reply_markup=kb)


@bot.callback_query_handler(func=lambda call: call.data == 'fly frugivores')
def question_22(call: types.CallbackQuery):
    kb = types.InlineKeyboardMarkup(row_width=1)
    btn1 = types.InlineKeyboardButton(text='Наезжаю грубым голосом', callback_data='Dracula parrot')
    btn2 = types.InlineKeyboardButton(text='Передразниваю', callback_data='pinkandgreycockatoo')
    kb.add(btn1, btn2, )
    bot.send_message(call.message.chat.id,
                     'Как вы ведете себя во время ссоры?',
                     reply_markup=kb)


@bot.callback_query_handler(func=lambda call: call.data)
def checking_answers(call: types.CallbackQuery):
    if call.data == 'indian_lion':
        url = 'https://storage.moscowzoo.ru/storage/647edc2a70bb5462366280fc/images/animals/114939dc-d35b-4999-a317-9858875cf56c.jpeg'
        bot.send_photo(call.message.chat.id, photo=(url), caption=f"О, да вы ЛЕВ!\n{animals['indian_lion']}")
    elif call.data == 'the_marten':
        url = ''
        bot.send_message(call.message.chat.id, "Вы лесная куница", )
    elif call.data == 'The_jackal':
        url = ''
        bot.send_message(call.message.chat.id, "Ой кажется Вы шакал", )
    elif call.data == 'manul':
        url = ''
        bot.send_message(call.message.chat.id, "О да Вы Манул", )
    elif call.data == 'capybara':
        url = ''
        bot.send_message(call.message.chat.id, "Вы капибара", )
    elif call.data == 'tamarin':
        url = ''
        bot.send_message(call.message.chat.id, "О да Вы золотистый львиный тамарин", )
    elif call.data == 'giraffe':
        url = ''
        bot.send_message(call.message.chat.id, "Вы дикдик", )
    elif call.data == 'dicdic':
        url = ''
        bot.send_message(call.message.chat.id, "О да Вы сетчатый жираф", )
    elif call.data == 'The scribe':
        url = ''
        bot.send_message(call.message.chat.id, "Вы Писец", )
    elif call.data == 'lynx':
        url = ''
        bot.send_message(call.message.chat.id, "Да вы Рысь", )
    elif call.data == 'manul_s':
        url = ''
        bot.send_message(call.message.chat.id, "Ой да Вы манул", )
    elif call.data == 'polar bear':
        url = ''
        bot.send_message(call.message.chat.id, "Вы Белый медведь", )
    elif call.data == 'walrus':
        url = ''
        bot.send_message(call.message.chat.id, "Вы морж", )
    elif call.data == 'larga':
        url = ''
        bot.send_message(call.message.chat.id, "Да Вы ларга", )
    elif call.data == 'The blue ram':
        url = ''
        bot.send_message(call.message.chat.id, "Ой да вы голубой баран", )
    elif call.data == 'navy seal':
        url = ''
        bot.send_message(call.message.chat.id, "Вы морской котик", )
    elif call.data == 'Snowy owl':
        url = ''
        bot.send_message(call.message.chat.id, "Да вы Снежная сова", )
    elif call.data == 'Mallard':
        url = ''
        bot.send_message(call.message.chat.id, "Вы кряква", )
    elif call.data == 'Jackass penguin':
        url = ''
        bot.send_message(call.message.chat.id, "Да вы Очковый пингвин", )
    elif call.data == 'Gentoo penguin':
        url = ''
        bot.send_message(call.message.chat.id, "Вы папуанский пингвин", )
    elif call.data == 'Lesser spotted eagle':
        url = ''
        bot.send_message(call.message.chat.id, "Вы Малый подорлик", )
    elif call.data == 'Long-eared owl':
        url = ''
        bot.send_message(call.message.chat.id, "Да вы длинно-ухая сова", )
    elif call.data == 'Dracula parrot':
        url = ''
        bot.send_message(call.message.chat.id, "Вы орлиный попугай", )
    elif call.data == 'pinkandgreycockatoo':
        url = ''
        bot.send_message(call.message.chat.id, "Вы розовый какаду", )


bot.polling()
