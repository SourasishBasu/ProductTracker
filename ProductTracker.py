import smtplib
import requests
from bs4 import BeautifulSoup

# Change the url string value below to the exact website (Amazon/Flipkart) link of the product you wish to track
url= 'https://www.flipkart.com/google-pixel-6a-charcoal-128-gb/p/itme5ae89135d44e?pid=MOBGFKX5YUXD74Z3&lid=LSTMOBGFKX5YUXD74Z3MXA2OB&marketplace=FLIPKART&sattr[]=color&st=color'
site_name = url.split(".")[1]

# Search 'my user agent' in your preferred browser and paste the information displayed within {} as below
headers = {"User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/116.0'}
page = requests.get(url, headers=headers)
soup = BeautifulSoup(page.content, 'html.parser')

#Change this value to the price you want compare the product's price against
threshold_amt = 27999

# Mail Function
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

# Product Stock Availability Function
def check_availability(site):
    if site == 'amazon':
        name = soup.find(id="productTitle").get_text().strip()
        avail = soup.find(id="priceblock_ourprice")
        if avail is not None:
            info = f"{name} is available in stock."
            send_email(info)

    if site == 'flipkart':
        name = soup.find("span", {"class": "B_NuCI"}).get_text().strip()
        avail = soup.find(id="pincodeInputId")
        if avail is not None:
            info = f"{name} is available in stock."
            send_email(info)

# Product Price Drop Function
def price_drop(site):
    if site == 'amazon':
        name = soup.find(id="productTitle").get_text().strip()
        price = float(soup.find('span', class_='a-price-whole').text.split()[0].replace(',', ""))
        final_price = int(price)

        if final_price < threshold_amt:
            info = f"Price of {name} on {site} has dropped to {final_price}."
            send_email(info)

    if site == 'flipkart':
        name = soup.find("span", {"class": "B_NuCI"}).get_text().strip()
        price = soup.find('div', attrs={"class": "_16Jk6d"}).text[1:].strip().replace(",", "")
        final_price = int(price)

        if final_price < threshold_amt:
            info = f"Price of {name} on {site.title()} has dropped to {final_price}."
            send_email(info)

# Use the following function calls as per your requirement
price_drop(site_name)
check_availability(site_name)

'''
# For various user controlled inputs

user = int(input("Enter 1 to check for price drop or 2 to check product in stock availability: "))

if user == 1:
    # normally this can be fixed in a constant before if it is automated as a script to check for a particular product
    threshold_amt = int(input("Enter price to check price drop of product against: "))
    price_drop(site_name)

elif user == 2:
    check_availability(site_name)

else:
    print("Invalid input. Run again.")
'''
