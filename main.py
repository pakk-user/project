from telebot import TeleBot, types

# Замените токен на ваш
BOT_TOKEN = "7748798267:AAGRvv-nS6ql0t7KqwitMeH4rjzXhdeJPvc"
WEB_APP_URL = "https://your-app-name.up.railway.app"  # Замените на URL вашего приложения

bot = TeleBot(BOT_TOKEN)


@bot.message_handler(commands=["start"])
def start(message):
    keyboard = types.InlineKeyboardMarkup()
    web_app_button = types.InlineKeyboardButton(
        text="запустить кликер", web_app=types.WebAppInfo(url=f"{WEB_APP_URL}?user_id={message.chat.id}")
    )
    keyboard.add(web_app_button)

    bot.send_message(
        message.chat.id,
        "привет, нажми на кнопку ниже.",
        reply_markup=keyboard
    )


bot.polling()