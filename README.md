# 💨 Internet Speed Twitter Bot

A Python automation script that checks your internet speed using **Speedtest.net** and automatically tweets at your Internet Service Provider (ISP) if your speed is slower than what you pay for.

---

## ⚙️ Features
- Measures **download** and **upload** speeds via Speedtest.net.  
- Logs into **Twitter (X)** automatically.  
- Tweets at your provider with the results.  
- Uses environment variables for secure credential handling.  

---

## 🧰 Requirements
- **Python 3.8+**  
- **Google Chrome**  
- **ChromeDriver** (matching your Chrome version)  
- **pip** (Python package manager)  

---

## 🧩 Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/yourusername/internet-speed-twitter-bot.git
   cd internet-speed-twitter-bot
   ```

2. **Install dependencies:**
   ```bash
   pip install selenium python-dotenv
   ```

3. **Set up your `.env` file:**
   Create a `.env` file in the root directory and add:
   ```env
   TWITTER_EMAIL=youremail@example.com
   TWITTER_PASSWORD=yourpassword
   ```

4. **(Optional) Update your promised speeds:**
   Inside `main.py`, edit:
   ```python
   PROMISED_DOWN = 150
   PROMISED_UP = 10
   ```

---

## 🚀 Usage

Run the bot with:
```bash
python main.py
```

The bot will:
1. Open [Speedtest.net](https://www.speedtest.net/) and measure your current internet speed.  
2. Log into **Twitter (X)** using your credentials.  
3. Tweet a message like:  
   ```
   Hey Internet Provider, why is my internet speed 45 down / 5 up 
   when I pay for 150 down / 10 up?
   ```

---

## 🧠 Notes
- Ensure **ChromeDriver** is installed and added to your system PATH.  
- The script uses `detach=True` to keep Chrome open — remove that option if you want Chrome to close automatically.  
- Twitter/X updates its layout frequently — if elements change, you may need to update the CSS selectors in the code.  

---

## 🔒 Security
- Your Twitter credentials are stored locally in a `.env` file.  
- **Never commit your `.env` file to GitHub!**  

Add it to your `.gitignore` file:
```
.env
```

---

## 👨‍💻 Author
**Your Name**  
📧 [your.email@example.com]  
🐙 [GitHub](https://github.com/yourusername)

---

## 📜 License
This project is licensed under the **MIT License** — feel free to use and modify it.
