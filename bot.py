from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, ContextTypes, CallbackQueryHandler
import os
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv("TOKEN")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [
            InlineKeyboardButton("🌿 About Me", callback_data="about")
        ],
        [
            InlineKeyboardButton("💻 My Skills", callback_data="skills"),
            InlineKeyboardButton("🚀 My Projects", callback_data="projects")
        ],
        [
            InlineKeyboardButton("🔗 My Links", callback_data="links"),
            InlineKeyboardButton("📩 Contact Me", callback_data="contact")
        ]
    ]

    reply_markup = InlineKeyboardMarkup(keyboard)

    await update.message.reply_text(
        "🌸 Welcome to MiMi Bot! 🤖💗\n\n"
        "Choose what you want 👇✨",
        reply_markup=reply_markup
    )

async def button_click(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    if query.data == "skills":
        await query.message.reply_text(
            "💻 My Skills\n\n"
            "🌐 HTML5 & CSS3\n"
            "⚡ Vanilla JavaScript (ES6+)\n"
            "💜 C# — OOP & Programming\n"
            "🎨 UI/UX Design & Glassmorphism\n"
            "🔗 REST APIs Integration\n"
            "🔧 Git & GitHub Version Control\n"
            "🤖 Python & Telegram Bots"
        )

    elif query.data == "projects":
        await query.message.reply_text(
            "🚀 My Projects\n\n"
            "🌟 Personal Portfolio — Modern responsive portfolio website\n"
            "🌙 Azan App — Real-time prayer times & Hijri converter\n"
            "🌿 Weather & Astronomy — Live forecast with NASA moon phases\n"
            "🌿 Task Tracker — Minimalist productivity app with subtasks\n"
            "🎴 Memory Card Game — Interactive 3D flip card game\n"
            "👁️ The Stalking Eyes — Trigonometric cursor-tracking eyes\n"
            "🧠 Tiny Quiz App — Interactive web assessment & scoring\n"
            "💚 HerzHilfe — Modern responsive non-profit landing page\n"
            "🤖 MiMi Telegram Bot — Interactive portfolio bot\n"
            "💜 C# University Coursework Projects"
        )

    elif query.data == "about":
        await query.message.reply_text(
            "🌿 About Me\n\n"
            "Hi! I'm Aman 🤍\n"
            "🎓 IT Engineering Student\n"
            "💻 Passionate Front-End Developer\n"
            "🎨 UI/UX Enthusiast\n"
            "🤖 Exploring AI & Automation"
        )

    elif query.data == "contact":
        await query.message.reply_text(
            "📩 Contact Me\n\n"
            "📧 Email: aman.aldaher.4@gmail.com\n"
            "📱 Telegram: @Alaman_com\n\n"
            "✨ Feel free to contact me!"
        )

    elif query.data == "links":
        keyboard = [
            [
                InlineKeyboardButton(
                    "🌐 Portfolio Website",
                    url="https://amanaldaher.github.io/Personal_Portfolio/"
                )
            ],
            [
                InlineKeyboardButton(
                    "📸 Instagram",
                    url="https://www.instagram.com/aman_aldaher/"
                )
            ],
            [
                InlineKeyboardButton(
                    "💻 GitHub",
                    url="https://github.com/amanaldaher"
                )
            ],
            [
                InlineKeyboardButton(
                    "💼 LinkedIn",
                    url="https://www.linkedin.com/in/aman-aldaher"
                )
            ],
            [
                InlineKeyboardButton(
                    "📱 Telegram",
                    url="https://t.me/Alaman_com"
                )
            ]
        ]

        reply_markup = InlineKeyboardMarkup(keyboard)

        await query.message.reply_text(
            "🔗 My Links\n\n"
            "Find me here 👇✨",
            reply_markup=reply_markup
        )

app = Application.builder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(CallbackQueryHandler(button_click))

print("Bot is running... 🤖")

app.run_polling()