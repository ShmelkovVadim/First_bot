import logging                                                                          # Добавляем для того что бы нам в консоль показывало ошибку, в случае неккоректной работы в боте
from telegram.ext import (Updater,CommandHandler, MessageHandler, Filters)                      # updater он отвечает за прием и передачу информации с тг
# КоммандХендлер(обработчик) он обрабатывает только команды ; MessageHandler реагирует только на текст

import settings                                                                        #Спрятали ссылку

logging.basicConfig(filename="bot.log", level=logging.INFO, format='%(asctime)s.%(msecs)03d %(levelname)s %(module)s - %(funcName)s: %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S')                                                      # Пишем о том что мы хотим сделать с сообщениями об ошибках,в какой файл,а level уровень важности сообщений,я указал формат еще


def greet_user(update, context):
    print("Вызван /start")                                                            # Тут через print показываем,что нам будет отображаться в командной строке после нажатия на start
    update.message.reply_text("Привет!")                                              # Тут мы указали,что отвечает наш бот после команды /start

def talk_to_me(update, context):
    text = update.message.text                                                        # Получаем тот текст который прислал нам пользователь
    print(text)                                                                       # Сделали принт в консоль
    update.message.reply_text(text)                                                   # Отпаравляем пользователю его же сообщение

def main():
    mybot = Updater(settings.API_KEY, use_context=True)

    dp = mybot.dispatcher                                                            # Диспечер моего бота
    dp.add_handler(CommandHandler("start", greet_user))                              # add_handler - Добавляем обработчик(команду) в нашем случае srart
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))

    mybot.start_polling()                                                            # Он отправляет запрос в тг не отправили ли команду в бот
    mybot.idle()                                                                     # Что бы бот работал без остановки пока сами не выключим


if __name__=="__main__":
    main()                                                                               # Именно main запускает бота
