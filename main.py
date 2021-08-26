import logging
from telegram.ext import Updater,MessageHandler, Filters,CommandHandler
from telegram import Bot

logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')


class TelegramController:
    TOKEN = '1941098188:AAEZi-cp4GpRxOPMjZ5aB2lABx8irl-iTyU'

    def __init__(self):
        self.logger = logging.getLogger()
        self.logger.setLevel(logging.INFO)
        self.updater = Updater(token=self.TOKEN, use_context=True)
        dispatcher = self.updater.dispatcher
        self.configure_handlers(dispatcher)

    def run(self):
        self.updater.start_polling()

    def configure_handlers(self, dispatcher):
        start_handler = CommandHandler('start', self.start)
        dispatcher.add_handler(start_handler)

        echo_handler = MessageHandler(Filters.text & (~Filters.command),  self.echo)
        dispatcher.add_handler(echo_handler)

        image_handler = MessageHandler(Filters.photo ,  self.photo_echo)
        dispatcher.add_handler(image_handler)

        caps_handler = CommandHandler('caps',  self.caps)
        dispatcher.add_handler(caps_handler)

        s_math_handler = CommandHandler('simple_math',  self.simple_math)
        dispatcher.add_handler(s_math_handler)

    def start(self, update, context):
        context.bot.send_message(chat_id=update.effective_chat.id, text="I'm a bot, please talk to me!")

    def echo(self, update, context):
        context.bot.send_message(chat_id=update.effective_chat.id, text=update.message.text)

    def photo_echo(self, update, context):
        context.bot.send_message(chat_id=update.effective_chat.id, text="Image was received")

    def caps(self, update, context):
        text_caps = ' '.join(context.args).upper()
        context.bot.send_message(chat_id=update.effective_chat.id, text=text_caps)

    def simple_math(self, update, context):
        v = update.message.text.split(' ')
        v.pop(0)
        result = 0
        message = "{} = {}"
        context.bot.send_message(chat_id=update.effective_chat.id, text=message.format("".join(v), result))


obj = TelegramController()

obj.run()