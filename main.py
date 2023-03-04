import telebot 
bot = telebot.TeleBot("5383742366:AAHl0NjQHH420ej2XYxhm4aAOMhJ2ttGpgE")



@bot.message_handler(commands=["start"])
def reply(message):
          name = message.from_user.first_name
          id = message.from_user.id

          mention= f"[{name}](tg://user?id={id})"
          bot.reply_to(message, f"اهلا بك {mention} \n وظيفة البوت زيادة المجموعة عن طريق تكرار الرسائل", parse_mode='markdown')


@bot.message_handler(func=lambda m : True)
def rm(m):
    if m.text=="المطور":
        bot.reply_to(m,"t.me/ddssss")
    elif m.text=="asta":
          bot.reply_to(m,"@ddssss")
    elif m.text=="استا":
          bot.reply_to(m,"t.me/ddssss")
    else:
        bot.reply_to(m,m.text)



bot.infinity_polling()