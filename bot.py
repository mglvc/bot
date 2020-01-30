import telebot
import time
import datetime

counter = 0
flag = [0, 0, 0, 0, 0, 0]
Apha_id =  #id человека, которого я поздравляю


bot = telebot.TeleBot()#в скобках должно быть айди бота



@bot.message_handler(commands=['start'])
def start_message(message):
	mid = message.chat.id
	bot.send_message(message.chat.id, 'Привет, Зай')
	time.sleep(0.3)
	bot.send_message(message.chat.id, 'Cегодня у тебя день рождения, и я, помимо прочего, решила сделать для тебя небольшого бота')


@bot.message_handler(commands=['counter'])
def start_message(message):
	#time.sleep(0.1)
	global counter
	if counter == 6:
		bot.send_message(message.chat.id, "ты нашел все пасхалки✨")
	elif counter >= 5:
		bot.send_message(message.chat.id, 'Ты нашел ' + str(counter) + " пасхалок")
	elif counter == 0:
		bot.send_message(message.chat.id, "ты не нашел ни одной пасхалки")
	elif counter == 1:
		bot.send_message(message.chat.id, 'Ты нашел ' + str(counter) + " пасхалку")
	else:
		bot.send_message(message.chat.id, 'Ты нашел ' + str(counter) + " пасхалки")

@bot.message_handler(commands=['help'])
def start_message(message):
	#time.sleep(0.1)
    bot.send_message(message.chat.id, 'Что я могу? Ну, например,поздравить тебя с днем рождения. Если ты напишешь число от 0 до 10, произойдет магия')

@bot.message_handler(commands=['time'])
def start_message(message):
	#time.sleep(0.1)

	aa = datetime.datetime(2019, 3, 8)
	now = datetime.datetime.now()
	cc = now-aa
	t = str(cc.days) + ' дней ^^'

	bot.send_message(message.chat.id, 'мы вместе ' +  t)

@bot.message_handler(content_types=['text'])
def send_text(message):
	global counter
	global flag

	mid = message.chat.id
	global Apha_id
	if (mid == Apha_id):
		if message.text.lower() == '0':
			bot.send_message(message.chat.id, '10 причин, почему я люблю тебя. Продолжать можно бесконечно, но...')
		elif message.text.lower() == '1':
			bot.send_message(message.chat.id, 'Ты очень заботливый. Я уверена в тебе на 100%, знаю, что ты всегда заваришь чай, съешь еду, которую я не ем и отнесешь на ручках, если я не могу ходить сама')
		elif message.text.lower() == '2':
			bot.send_message(message.chat.id, 'Ты поддерживаешь все мои идиотские идеи')
		elif message.text.lower() == '3':
			bot.send_message(message.chat.id, 'В твоих объятиях хорошо и уютно')
		elif message.text.lower() == '4'
			bot.send_message(message.chat.id, 'Мне очень хорошо с тобой')
		elif message.text.lower() == '5':
			bot.send_message(message.chat.id, 'Мы можем говорить обо всем и ни о чем')
		elif message.text.lower() == '6':
			bot.send_message(message.chat.id, 'Вместе мы можем творить чудеса и ломать мир')
		elif message.text.lower() == '7':
			bot.send_message(message.chat.id, 'Не хочу выпускать тебя из объятий')
		elif message.text.lower() == '8':
			bot.send_message(message.chat.id, 'Потому что ты мое чудо')
		elif message.text.lower() == '9':
			bot.send_message(message.chat.id, 'Когда ты рядом, мир вокруг расцветает')
		elif message.text.lower() == '10':
			bot.send_message(message.chat.id, 'Потому что ты всегда мне поможешь')

		elif message.text.lower() == 'я люблю тебя':
			if flag[0] == 0:
				flag[0] = 1;
				counter += 1
			bot.send_message(message.chat.id, 'Я тебя тоже, Зай')
		elif message.text.lower() == 'люблю тебя':
			if flag[0] == 0:
				flag[0] = 1;
				counter += 1
			bot.send_message(message.chat.id, 'аналогично <3')
		elif message.text.lower() == 'мявк':
			if flag[1] == 0:
				flag[1]== 1
				counter += 1
			bot.send_message(message.chat.id, 'мур?')
		elif message.text.lower() == 'я тебя люблю':
			if flag[0] == 0:
				flag[0] = 1;
				counter += 1
			bot.send_message(message.chat.id, 'Я тебя тоже люблю, Зай')
		elif message.text.lower() == 'акула':		
			if flag[2] == 0:
				flag[2] = 1
				counter += 1
			bot.send_message(message.chat.id, 'Воспитываю твою акулу с 22 декабря, ахах')
		elif message.text.lower() == '42':
			if flag[3] == 0:
				flag[3]= 1
				counter += 1
			bot.send_message(message.chat.id, "Это ответ на главный вопрос жизни, вселенной и всего остального. Don't panic")

		elif message.text.lower() == 'спасибо':		
			if flag[6] == 0:
				flag[6]= 1
				counter += 1 
			bot.send_message(message.chat.id, "не за что, Зай")
		else:
			if flag[7] == 0:
				counter += 1
				flag[7] += 1
			bot.send_message(message.chat.id, 'Решил сломать систему? Я все учла! <3')
	else:
		bot.send_message(message.chat.id, 'не для тебя писался этот бот')
bot.polling()
