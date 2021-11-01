#!/usr/bin/env python
# pylint: disable=C0116,W0613
# This program is dedicated to the public domain under the CC0 license.

"""
Simple Bot to reply to Telegram messages.

First, a few handler functions are defined. Then, those functions are passed to
the Dispatcher and registered at their respective places.
Then, the bot is started and runs until we press Ctrl-C on the command line.

Usage:
Basic Echobot example, repeats messages.
Press Ctrl-C on the command line or send a signal to the process to stop the
bot.
"""
import mysql.connector

conexion = mysql.connector.connect(user='root', password='sAyonAr428.',host='localhost',database='prueba_asistenciati',port='3306')
print(conexion)
cursor = conexion.cursor() #con cursor podré ejecutar la consulta a la BD

import logging

from telegram import Update, ForceReply
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext

# Enable logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)

logger = logging.getLogger(__name__)


# Define a few command handlers. These usually take the two arguments update and
# context.
def start(update: Update, context: CallbackContext) -> None:
    """Send a message when the command /start is issued."""
    user = update.effective_user
    update.message.reply_markdown_v2(
        fr'Hi {user.mention_markdown_v2()}\!',
        reply_markup=ForceReply(selective=True),
    )


def help_command(update: Update, context: CallbackContext) -> None:
    """Send a message when the command /help is issued."""
    update.message.reply_text('Help!')


def echo(update: Update, context: CallbackContext) -> None:
    """Echo the user message."""
    update.message.reply_text(update.message.text)
def pizza (update, context):
    if(update.message.text.upper().find("MANZANAS VERDES") > 0):
        update.message.reply_text("prefiero comer pizza")

def sumar(update,context):
    try:
        numero1 = int(context.args[0])
        numero2 = int(context.args[1])
        suma = numero1 + numero2
        update.message.reply_text("La suma es: "+str(suma))
    except (ValueError):
        update.message.reply_text("error")

def consulta(update:Update, context: CallbackContext) -> None:
    """Contestar al usuario."""
    update.message.reply_text("Favor de seleccionar la opción por la que desea consultar: \nRegión \nTicket \nTienda \nFalla \nSi desea salir del menú, solo teclee /salir \nPara volver al inicio, solo teclee /inicio")
    #if (update.message.reply_text == 'region'):
    #    update.message.reply_text("favor de teclear la nomenclatura de la region")
    #respuesta = int(update.message.find()):
    #if respuesta == 1:
        #update.message.reply_text("Favor de proporcionar la nomenclatura de la región")
    #if respuesta == 2:
        #update.message.reply_text("Favor de proporcionar el número de ticket")
        #print("Hello")
def region(update:Update, context: CallbackContext) -> None:
    """Consultar incidencia por región"""
    update.message.reply_text("Favor de proporcionar la nomenclatura de la región a 4 letras")

#def consultarregion(palabraclave):
#    consulta = palabraclave
#    cursor.execute("Select * from reporte r, region rg where r.id_region = rg.id_region and nomenclatura_reg like " + "'%" + consulta +"'")
#    dispatcher.add_handler(CommandHandler("consultaregion", consultaregion))

def ticket(update:Update, context: CallbackContext) -> None:
    """Consultar incidencia por número de ticket"""
    update.message.reply_text("Favor de teclear el número de ticket de Asistencia TI")
def tienda(update:Update, context: CallbackContext) -> None:
    """Consultar por número de Tienda"""
    update.message.reply_text("Favor de teclear el número de Tienda a 4 dígitos")
def falla(update:Update, context: CallbackContext) -> None:
    """Consultar por nomobre de la falla"""
    update.message.reply_text("Favor de teclear el nombre de la falla")
def salir(update:Update, context: CallbackContext) -> None:
    """Opción para salir del menú y decir la despedida"""
    update.message.reply_text("Muchas gracias por utilizar el chatbot de CEMIC. \n¡Hasta pronto!")
def inicio(update:Update, context: CallbackContext) -> None:
    """Opción para regresar al inicio del chat"""
    user = update.effective_user
    update.message.reply_markdown_v2(
        fr'Hi {user.mention_markdown_v2()}\!',
        reply_markup=ForceReply(selective=True),
    )

def main() -> None:

    # Create the Updater and pass it your bot's token.
    updater = Updater("2007607069:AAHhGQ2BnIlj2Dk7a52eglskQN287ZXApAQ")
#cambio
    # Get the dispatcher to register handlers
    dispatcher = updater.dispatcher

    # on different commands - answer in Telegram
    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CommandHandler("help", help_command))
    dispatcher.add_handler(CommandHandler("sumar", sumar))
    dispatcher.add_handler(CommandHandler("consulta", consulta))
    dispatcher.add_handler(CommandHandler("region", region))
    dispatcher.add_handler(CommandHandler("ticket", ticket))
    dispatcher.add_handler(CommandHandler("tienda", tienda))
    dispatcher.add_handler(CommandHandler("falla", falla))
    dispatcher.add_handler(CommandHandler("salir", salir))
    dispatcher.add_handler(CommandHandler("inicio", inicio))

    # on non command i.e message - echo the message on Telegram
    dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, pizza))

    # Start the Bot
    updater.start_polling()

    # Run the bot until you press Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
    updater.idle()


if __name__ == '__main__':
    main()
