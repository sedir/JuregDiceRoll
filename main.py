import telebot, datetime, time, random
from telebot import types
bot = telebot.TeleBot("#BOT_TOKEN_ID#")

def CheckDiceCall(d):
	#print(d)
	if d[0] == '*' and d[-1] == '*' and d[1] == 'd' and d[2:-1].isnumeric():
		return True
	else:
		return False

@bot.message_handler(commands=['d100'])
def d100(message):
	print("d100")
	roll = random.randrange(1,101)
	msg = "Rolagem: {}".format(roll)
	bot.send_message(message.chat.id, msg, reply_to_message_id=message.message_id)

@bot.message_handler(commands=['dicemenu'])
def dicemenu(message):
	rkm = types.ReplyKeyboardMarkup(row_width=3,one_time_keyboard=False,resize_keyboard=True)
	dices = ['*d100*','*d4*','*d6*','*d8*','*d10*','*d12*','*d20*']
	rkm.add(dices[0])
	rkm.row(dices[1],dices[2],dices[3])
	rkm.row(dices[4],dices[5],dices[6])
	msg = "Escolha um dado para rolar"
	bot.send_message(message.chat.id, msg, reply_markup=rkm)

@bot.message_handler(func=lambda message: CheckDiceCall(message.text), content_types=["text"])
def bot_pedidos(message):
	print(message.chat.id)
	dice = int(message.text[2:-1])+1
	roll = random.randrange(1,dice)
	msg = "Rolagem: {}".format(roll)
	bot.send_message(message.chat.id, msg, reply_to_message_id=message.message_id)

print("Starting Telegram Bot")
bot.polling(none_stop=True, interval=0)