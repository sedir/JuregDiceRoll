import random

import telebot
from loguru import logger
from telebot import types

from config import settings


bot = telebot.TeleBot(settings.TOKEN)


def check_dice_call(d):
    try:
        if d[0] == "*" and d[-1] == "*" and d[1] == "d" and d[2:-1].isnumeric():
            return True
        else:
            return False
    except NameError:
        logger.exception(f"Error getting from mesage: {d}")
        return False


@bot.message_handler(commands=["d100"])
def d100(message):
    roll = random.randrange(1, 101)
    msg = f"Rolagem: {roll}"
    bot.send_message(message.chat.id, msg, reply_to_message_id=message.message_id)
    logger.info(f"Chat: {message.chat.id}, Command: /d100, Roll: {roll}")


@bot.message_handler(commands=["dicemenu"])
def dicemenu(message):
    rkm = types.ReplyKeyboardMarkup(
        row_width=3, one_time_keyboard=False, resize_keyboard=True
    )
    dices = ["*d100*", "*d4*", "*d6*", "*d8*", "*d10*", "*d12*", "*d20*"]
    rkm.add(dices[0])
    rkm.row(dices[1], dices[2], dices[3])
    rkm.row(dices[4], dices[5], dices[6])
    msg = "Escolha um dado para rolar"
    bot.send_message(message.chat.id, msg, reply_markup=rkm)
    logger.info(f"Chat: {message.chat.id}, Command: /dicemenu")


@bot.message_handler(
    func=lambda message: check_dice_call(message.text), content_types=["text"]
)
def bot_pedidos(message):
    dice = int(message.text[2:-1]) + 1
    roll = random.randrange(1, dice)
    msg = f"Rolagem: {roll}"
    bot.send_message(message.chat.id, msg, reply_to_message_id=message.message_id)
    logger.info(f"Chat: {message.chat.id}, Roll: {roll}")


if __name__ == "__main__":
    logger.info("Starting Telegram Bot")
    bot.polling(none_stop=True, interval=0)
