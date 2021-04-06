import Constants as keys

from telegram import *
from telegram.ext import *

import Responses as R

def start_command(update, context):
	update.message.reply_text('Mokhles Bhai er sathe kotha bolte chaile kichu lekh, Banglish a likhbi r Taakla vasha cholbena. Tui kore kotha bolbi')

def help_command(update, context):
	update.message.reply_text('need to know something? Search google')


def handle_message(update, context):
	text = str(update.message.text).lower()
	response = R.sample_responses(text)

	update.message.reply_text(response)

def error(update, context):
	print(f"Update {Update} caused error {context.error}")

def main():
	updater = Updater(keys.API_KEY, use_context = True)
	dp = updater.dispatcher

	dp.add_handler(CommandHandler("Start", start_command))
	dp.add_handler(CommandHandler("Start", help_command))

	dp.add_handler(MessageHandler(Filters.text, handle_message))

	dp.add_error_handler(error)

	updater.start_polling(0)
	updater.idle()

main()