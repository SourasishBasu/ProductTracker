import smtplib
from selenium import webdriver
from bs4 import BeautifulSoup

url = 'https://www.thesouledstore.com/product/solids-mandarin-polo-navy?gte=0'

driver = webdriver.Firefox()
headers = {"User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/116.0'}
driver.get(url)
html = driver.page_source
soup = BeautifulSoup(html, "html.parser")
items = soup.find_all('label', {'for': '2'})


def send_email(info):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()

    server.login('YOUR_EMAIL', 'EMAIL_APP_PASSWORD')

    subject = "Product is available"
    body = f"{info}\nCheck this link: {url}"
    msg = f"Subject:{subject}\n\n{body}"

    server.sendmail('SENDERS_EMAIL', 'RECEIVERS_MAIL', msg)

    print("Hey, email has been sent!")
    server.quit()


def check():
    tags = ""
    for tag in items:
        tag = str(tag)
        tag = tag.replace("<", "").replace(">", "").replace(" ", ",")
        tags += tag

    scripts = tags.split(",")

    if "" in scripts[1]:
        info = "Size M of the Solid Navy Mandarin Polo is in stock."
        send_email(info)
    elif "strikethrough" in scripts[1]:
        info = "Product is yet to be available in store."

check()
