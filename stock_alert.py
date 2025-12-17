import requests
import smtplib
import os

# CONFIGURATION
API_KEY = os.environ["API_KEY"]
SYMBOL = "NVDA"          # change later
TARGET_PRICE = 180.0    # change later

EMAIL = os.environ["EMAIL"]
EMAIL_PASSWORD = os.environ["EMAIL_PASSWORD"]

def get_stock_price():
    url = (
        "https://www.alphavantage.co/query"
        f"?function=GLOBAL_QUOTE&symbol={SYMBOL}&apikey={API_KEY}"
    )
    data = requests.get(url).json()
    return float(data["Global Quote"]["05. price"])

def send_email(price):
    message = f"""Subject: Stock Alert 🚨

{SYMBOL} price reached {price}
Target price was {TARGET_PRICE}
"""

    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
        server.login(EMAIL, EMAIL_PASSWORD)
        server.sendmail(EMAIL, EMAIL, message)

price = get_stock_price()
print("Current price:", price)

if price <= TARGET_PRICE:
    send_email(price)
    print("Email sent!")
else:
    print("Condition not met")
