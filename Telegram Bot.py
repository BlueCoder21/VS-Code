

import telegram.ext
import requests
import json
from telegram.ext.updater import Updater
from telegram.ext.commandhandler import CommandHandler
from telegram.ext.messagehandler import MessageHandler
from telegram.ext.filters import Filters

updater = Updater(token="5130350267:AAFVQ8NCO3ufvYcJ7Tm7S8SA5ViSGh4GYAU",use_context = True)
dispatcher = updater.dispatcher

def hello(update,context):
    context.bot.send_message(chat_id=update.effective_chat.id,text="Hello Mayank")
    hello_handler = CommandHandler("hello",hello)
    dispatcher.add_handler(hello_handler)

updater.start_polling()

def summary(update,context):
    response = requests.get('https://api.covid19api.com/summary')
    if(response.status_code==200):
        data = response.json()
        date = data["Date"][:10]
        ans = f"Covid 19 Summary(as of {date}): \n";
        for attribute,value in data["Global"].items():
            if attribute not in["NewConfirmed","NewDeaths","NewRecovered"]:
                ans += "Total"+attribute[5::].lower()+":"+str(value)+ "\n"
        print(ans)
        context.bot.send_message(chat_id=update.effective_chat.id,text=ans)
    else:
        context.bot.send_message(chat_id=update.effective_chat.id,text="Error,Something went wrong")

corona_summary_handler = CommandHandler('summary',summary)
dispatcher.add_handler(corona_summary_handler)

