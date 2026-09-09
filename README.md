# 🤖 MiMi — Personal Portfolio Telegram Bot

[![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![python--telegram--bot](https://img.shields.io/badge/python--telegram--bot-v20%2B-2CA5E0?style=for-the-badge&logo=telegram&logoColor=white)](https://python-telegram-bot.org/)
[![Git](https://img.shields.io/badge/Git-F05032?style=for-the-badge&logo=git&logoColor=white)](https://git-scm.com/)

An interactive asynchronous Telegram bot built with **Python 3** and the **python-telegram-bot (v20+)** library. 

**MiMi Bot** serves as an interactive digital portfolio and networking hub, allowing visitors on Telegram to explore skills, browse key projects, review professional bio details, and access direct social links through responsive inline keyboard menus.

---

## 🚀 Try The Bot

Chat with MiMi live on Telegram:  
👉 **[Open @MiMispark_bot](https://t.me/MiMispark_bot)**

---

## 📌 Key Features

- **Asynchronous Architecture:** Built using modern `async/await` patterns with `ApplicationBuilder` for high responsiveness.
- **Interactive Inline Keyboards:** Intuitive button navigation (`InlineKeyboardMarkup`) eliminating the need to type manual commands.
- **Dynamic Portfolio Sections:**
  - 🌿 **About Me:** Professional background and academic focus.
  - 💻 **My Skills:** Core competencies across Web Development, C#, UI/UX, and AI.
  - 🚀 **My Projects:** Showcase of highlighted software projects.
  - 🔗 **My Links:** Direct URL buttons to LinkedIn, GitHub, Instagram, and Telegram.
  - 📩 **Contact Me:** Direct communication channels.
- **Security-First Configuration:** Secures the bot API token using environment variables (`python-dotenv`) and strict `.gitignore` rules to keep credentials safe from public repository leaks.

---

## 🛠️ Built With

- **[Python 3.x](https://www.python.org/):** Core application language.
- **[python-telegram-bot](https://python-telegram-bot.org/):** Framework for interacting with the Telegram Bot API.
- **[python-dotenv](https://pypi.org/project/python-dotenv/):** Managing sensitive environment variables via `.env`.

---

## 📂 Project Structure

```text
├── .gitignore          # Prevents tracking secrets (.env), virtualenvs, and bytecode
├── bot.py              # Main bot logic, handlers, and inline keyboard controllers
├── requirements.txt    # Package dependencies
└── README.md           # Repository documentation
