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


# инфо об опеке
@bot.message_handler(commands=['info'])
def info(message: telebot.types.Message):
    text = 'В зоопарке действует программа "Возьми животное под опеку"\n'
    'Подробности по ссылке: \n'
    'https://moscowzoo.ru/my-zoo/become-a-guardian/'
    bot.send_message(message.chat.id, text)


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
        url = 'https://storage.moscowzoo.ru/storage/647edc2a70bb5462366280fc/images/animals/898b8719-43fd-4438-b184-334b0ec62cb4.jpg'
        bot.send_photo(call.message.chat.id, photo=(url), caption=f"Вы лесная куница\n{animals['the_marten']}")
    elif call.data == 'The_jackal':
        url = 'https://storage.moscowzoo.ru/storage/647edc2a70bb5462366280fc/images/animals/3aed64d4-c54a-44de-a527-30e097b39f98.jpg'
        bot.send_photo(call.message.chat.id, photo=(url), caption=f"Ой кажется Вы шакал\n{animals['The_jackal']}")
    elif call.data == 'manul':
        url = 'https://storage.moscowzoo.ru/storage/647edc2a70bb5462366280fc/images/animals/d7b75e62-45e5-4a75-a3b1-17dbb31e6fea.jpeg'
        bot.send_photo(call.message.chat.id, photo=(url), caption=f"О да Вы Манул\n{animals['manul']}")
    elif call.data == 'capybara':
        url = 'https://storage.moscowzoo.ru/storage/647edc2a70bb5462366280fc/images/animals/df1e1de9-6e0f-49aa-a019-14d9d320e0c4.jpg'
        bot.send_photo(call.message.chat.id, photo=(url), caption=f"Вы капибара\n{animals['capybara']}")
    elif call.data == 'tamarin':
        url = 'https://storage.moscowzoo.ru/storage/647edc2a70bb5462366280fc/images/animals/8e224d32-0cb7-4588-a942-710ce9a2b8aa.jpeg'
        bot.send_photo(call.message.chat.id, photo=(url), caption=f"О да Вы золотистый львиный тамарин\n{animals['tamarin']}")
    elif call.data == 'giraffe':
        url = 'https://storage.moscowzoo.ru/storage/647edc2a70bb5462366280fc/images/animals/1699340a-0f5a-46e8-97ea-98491d374584.jpg'
        bot.send_photo(call.message.chat.id, photo=(url), caption=f"О да Вы сетчатый жираф\n{animals['giraffe']}")
    elif call.data == 'dicdic':
        url = 'https://storage.moscowzoo.ru/storage/647edc2a70bb5462366280fc/images/animals/6de41b59-e76e-46a2-a18b-ec04f7f27bbc.jpeg'
        bot.send_photo(call.message.chat.id, photo=(url), caption=f"Вы дикдик\n{animals['dicdic']}")
    elif call.data == 'The scribe':
        url = 'https://storage.moscowzoo.ru/storage/647edc2a70bb5462366280fc/images/animals/c41d53da-8b31-4c2b-9011-01cccc81a899.jpg'
        bot.send_photo(call.message.chat.id, photo=(url), caption=f"Вы Писец\n{animals['The scribe']}")
    elif call.data == 'lynx':
        url = 'https://storage.moscowzoo.ru/storage/647edc2a70bb5462366280fc/images/animals/db07be03-f66e-4a59-9d77-b84a717b7d31.jpeg'
        bot.send_photo(call.message.chat.id, photo=(url), caption=f"Да вы Рысь\n{animals['lynx']}")
    elif call.data == 'manul_s':
        url = 'https://storage.moscowzoo.ru/storage/647edc2a70bb5462366280fc/images/animals/d7b75e62-45e5-4a75-a3b1-17dbb31e6fea.jpeg'
        bot.send_photo(call.message.chat.id, photo=(url), caption=f"Ой да Вы манул\n{animals['manul_s']}")
    elif call.data == 'polar bear':
        url = 'https://storage.moscowzoo.ru/storage/647edc2a70bb5462366280fc/images/animals/22c1783b-0644-434d-9b35-2143c5505033.jpeg'
        bot.send_photo(call.message.chat.id, photo=(url), caption=f"Вы Белый медведь\n{animals['polar bear']}")
    elif call.data == 'walrus':
        url = 'https://storage.moscowzoo.ru/storage/647edc2a70bb5462366280fc/images/animals/3198de3d-df5f-47a2-9abe-529d2ef11623.jpeg'
        bot.send_photo(call.message.chat.id, photo=(url), caption=f"Вы морж\n{animals['walrus']}")
    elif call.data == 'larga':
        url = 'https://storage.moscowzoo.ru/storage/647edc2a70bb5462366280fc/images/animals/8e89039a-222e-4ae0-92f2-808dd3d4d76d.jpeg'
        bot.send_photo(call.message.chat.id, photo=(url), caption=f"Да Вы ларга\n{animals['larga']}")
    elif call.data == 'The blue ram':
        url = 'https://storage.moscowzoo.ru/storage/647edc2a70bb5462366280fc/images/animals/6c627b5f-b6c6-45b8-936a-b8d68b57eb56.png'
        bot.send_photo(call.message.chat.id, photo=(url), caption=f"Ой да вы голубой баран\n{animals['The blue ram']}")
    elif call.data == 'navy seal':
        url = 'https://storage.moscowzoo.ru/storage/647edc2a70bb5462366280fc/images/animals/9ce2f8cd-fb13-45a6-8853-4b9dea4af851.jpeg'
        bot.send_photo(call.message.chat.id, photo=(url), caption=f"Вы морской котик\n{animals['navy seal']}")
    elif call.data == 'Snowy owl':
        url = 'https://storage.moscowzoo.ru/storage/647edc2a70bb5462366280fc/images/animals/042d7c00-9abf-4553-9b3d-eedd08f72090.jpeg'
        bot.send_photo(call.message.chat.id, photo=(url), caption=f"Да вы Снежная сова\n{animals['Snowy owl']}")
    elif call.data == 'Mallard':
        url = 'https://storage.moscowzoo.ru/storage/647edc2a70bb5462366280fc/images/animals/abb0a482-03a2-4e8b-940e-a7d4ed50778c.jpeg'
        bot.send_photo(call.message.chat.id, photo=(url), caption=f"Вы кряква\n{animals['Mallard']}")
    elif call.data == 'Jackass penguin':
        url = 'https://storage.moscowzoo.ru/storage/647edc2a70bb5462366280fc/images/animals/68cec806-a690-49ca-842c-263dfb9dae44.jpeg'
        bot.send_photo(call.message.chat.id, photo=(url), caption=f"Да вы Очковый пингвин\n{animals['Jackass penguin']}")
    elif call.data == 'Gentoo penguin':
        url = 'https://storage.moscowzoo.ru/storage/647edc2a70bb5462366280fc/images/animals/2cd872b5-7f55-481e-a7d1-159c4d5f0ca2.jpeg'
        bot.send_photo(call.message.chat.id, photo=(url), caption=f"Вы папуанский пингвин\n{animals['Gentoo penguin']}")
    elif call.data == 'Lesser spotted eagle':
        url = 'https://storage.moscowzoo.ru/storage/647edc2a70bb5462366280fc/images/animals/837235d3-a5eb-4a10-943a-c04874710594.jpeg'
        bot.send_photo(call.message.chat.id, photo=(url), caption=f"Вы Малый подорлик\n{animals['Lesser spotted eagle']}")
    elif call.data == 'Long-eared owl':
        url = 'https://storage.moscowzoo.ru/storage/647edc2a70bb5462366280fc/images/animals/380f0859-78ba-463e-a7e5-daf7107e62aa.jpeg'
        bot.send_photo(call.message.chat.id, photo=(url), caption=f"Да вы длинно-ухая сова\n{animals['Long-eared owl']}")
    elif call.data == 'Dracula parrot':
        url = 'https://storage.moscowzoo.ru/storage/647edc2a70bb5462366280fc/images/animals/4e17576f-4082-4250-b405-1d8f987b28bd.jpeg'
        bot.send_photo(call.message.chat.id, photo=(url), caption=f"Вы орлиный попугай\n{animals['Dracula parrot']}")
    elif call.data == 'pinkandgreycockatoo':
        url = 'https://storage.moscowzoo.ru/storage/647edc2a70bb5462366280fc/images/animals/47eb38a5-b36f-49c0-bbaa-4b26d4cc7e92.jpeg'
        bot.send_photo(call.message.chat.id, photo=(url), caption=f"Вы розовый какаду\n{animals['pinkandgreycockatoo']}")


bot.polling()
