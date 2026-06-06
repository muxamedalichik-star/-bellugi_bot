from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ChatJoinRequestHandler, ContextTypes

BOT_TOKEN = "8767834593:AAGBV2IYjr-ij0uX-B8FiGYXEKxeUWEbXbQ"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Привет!")

async def join_request(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.chat_join_request.from_user.id

    await context.bot.send_message(
        chat_id=user_id,
        text="Для вступления в канал отправьте скриншот подписки на TikTok аккаунт."
    )

if __name__ == "__main__":
    app = ApplicationBuilder().token(BOT_TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(ChatJoinRequestHandler(join_request))

    print("Бот запущен...")
    app.run_polling()