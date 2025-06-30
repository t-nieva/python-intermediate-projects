# 💸 Amazon Price Tracker with Email Alert

A simple Python script that checks the price of a product 
and sends an email alert when it drops below a target value.

## 📦 Features

- Scrapes product price from a static demo page or a live Amazon URL
- Sends email notification via Gmail SMTP
- Uses `.env` file to protect sensitive credentials

## 🚀 Set environment variables

Create a .env file in the project root:

```
GMAIL_EMAIL=your@gmail.com
PASSWORD_APP_GMAIL=your_app_password
YAHOO_EMAIL=your_target@yahoo.com
```

🧪 Example
If the product price drops below $100, you will receive an email alert like:

Subject: Amazon Price Alert!

Instant Pot Duo Plus

is now $89.99

https://appbrewery.github.io/instant_pot/

📋 Notes
For Gmail, you must generate an App Password if using 2FA.

The Amazon site blocks bots; this script works best with the static demo URL for testing.
