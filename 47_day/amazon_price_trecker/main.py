from bs4 import BeautifulSoup
import requests
import smtplib
from dotenv import load_dotenv
import os
import time

start = time.time()

load_dotenv()

sender_email = os.getenv("GMAIL_EMAIL")
recipient_email = os.getenv("YAHOO_EMAIL")
password_app_gmail = os.getenv("PASSWORD_APP_GMAIL")

# *********************** Static site ***********************
URL = "https://appbrewery.github.io/instant_pot/"
# *********************** Live Amazon site ***********************
# LIVE_URL = "https://www.amazon.com/dp/B075CYMYK6?ref_=cm_sw_r_cp_ud_ct_FM9M699VKHTT47YD50Q6&th=1"

headers = {
    "Accept-Language": "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7,uk;q=0.6,bg;q=0.5",
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Safari/537.36",
}

try:
    response = requests.get(URL, headers=headers)
    response.raise_for_status()
    website_data = response.text
except requests.RequestException as e:
    print(f"[ERROR] Failed to fetch website page: {e}")
    exit(1)

soup = BeautifulSoup(website_data, "html.parser")

# *********************** Scraping instant pot price from static page ***********************
price = soup.find(class_="a-offscreen").get_text()
price_without_currency = price.split("$")[1]
price = float(price_without_currency)

# *********************** Email alert when the price is below preset value ***********************
target_price = 100
message_to_send = f"Instant Pot Duo Plus\nis now ${price}\n{URL}"
if price < target_price:
    print("[INFO] Connecting to SMTP...")
    with smtplib.SMTP("smtp.gmail.com", port=587, timeout=10) as connection:
        connection.starttls()
        print("[INFO] TLS started")
        connection.login(user=sender_email, password=password_app_gmail)
        print("[INFO] Logged in")
        connection.sendmail(from_addr=sender_email, to_addrs=recipient_email, msg=f"Subject: Amazon Price Alert!\n\n{message_to_send}")
        print("[INFO] Email sent")

print(f"[INFO] Execution time: {time.time() - start:.2f} seconds")
