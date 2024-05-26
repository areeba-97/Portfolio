import requests
from bs4 import BeautifulSoup
import smtplib

AMAZON_URL = "https://www.amazon.com/dp/B075CYMYK6?amp=undefined&ref_=cm_sw_r_cp_ud_ct_FM9M699VKHTT47YD50Q6&th=1"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/115.0.0.0 Safari/537.36 Edg/115.0.1901.183",
    "Accept-Language": "en-US,en;q=0.9",
}

MY_EMAIL = "areebaah.999@gmail.com"
PASSWORD = "jrseqqpagrxulkpv"

response = requests.get(url=AMAZON_URL, headers=headers)
content = response.text
# print(content)

soup = BeautifulSoup(content, "lxml")
price = soup.find(name="span", class_="a-offscreen").get_text()
split_price = price.split('$')[1]
price_as_float = float(split_price)
print(price_as_float)

title = soup.find(name="span", id="productTitle").get_text().strip()
BUY_Price = 70

if price_as_float < BUY_Price:
    message = f"{title} is now {price}"

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs="areebaaltaf97@gmail.com",
            msg=f"Subject:Amazon Price Alert\n\n{message}\n{AMAZON_URL}".encode("utf-8")
        )
