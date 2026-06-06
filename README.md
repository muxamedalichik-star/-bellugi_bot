# -bellugi_bot
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ChatMemberHandler, ContextTypes

BOT_TOKEN = "8767834593:AAGBV2IYjr-ij0uX-B8FiGYXEKxeUWEbXbQ"

# Команда /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Привет! Чтобы присоединиться к каналу, отправьте заявку на вступление.")

# Новый участник в канале
async def new_chat_member(update: Update, context: ContextTypes.DEFAULT_TYPE):
    member = update.chat_member.new_chat_member
    if member.status == "member":
        user_id = member.user.id
        await context.bot.send_message(
            chat_id=user_id,
            text="Для вступления в канал покажите скриншот, подтверждающий подписку на TikTok аккаунт."
        )

if __name__ == "__main__":
    app = ApplicationBuilder().token(BOT_TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(ChatMemberHandler(new_chat_member, ChatMemberHandler.CHAT_MEMBER))

    print("Бот запущен...")
    app.run_polling()