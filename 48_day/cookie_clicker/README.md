# 🍪 Cookie Clicker Bot with Selenium
This Python script automates gameplay for the Cookie Clicker game using Selenium.
It continuously clicks the cookie and purchases upgrades automatically for 5 minutes.

## 📌 Features
+ Automatically selects English language (if available)
+ Continuously clicks the big cookie 
+ Buys the most expensive available item every 5 seconds 
+ Runs for 5 minutes, then stops and prints the final cookie count

## 🚀 Requirements
+ Python 3.7+
+ Google Chrome browser
+ ChromeDriver compatible with your Chrome version
+ Required Python packages:

```bush
pip install selenium
```

## 🧠 How It Works
1. Opens the game site.
2. Tries to click the English language button.
3. Repeatedly clicks the cookie.
4. Every 5 seconds:
   + Checks your current cookies.
   + Attempts to buy the most expensive enabled product.
5. After 5 minutes, prints your final cookie count and exits.
