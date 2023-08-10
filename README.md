# ProductTracker
 
 Python scripts that use webscraping on various e-commerce websites such as Amazon, Flipkart and TheSouledStore to track product availability or price drops.

### Prerequisites:

- Python 3.7 & up
- Open Command prompt and type:

  ```bash
  pip install beautifulsoup4
  pip install requests
  pip install -U selenium
  ```
- Download the [Chromium Webdriver](https://chromedriver.chromium.org/downloads) for Google Chrome or [Geckodriver](https://github.com/mozilla/geckodriver/releases) for Mozilla Firefox

 ## Usage

 ProductTracker.py has the following features:
 - Can check whether a product is in stock on Amazon/Flipkart
 - Can check whether a product price has dropped on Amazon/Flipkart
 - Automatically sends a mail to specified gmail address upon success
<br> </br>

checkstock.py uses Selenium WebDriver to check whether a specific shirt size is available on TheSouledStore site. 
- I made this as an example since some websites are created via javascript after the initial HTML page has loaded into the browser.
- Requests is just an HTTP client, not a full-fledged browser engine, so it doesn't execute the Javascript that contains the element such as the shirt size from this website. Hence Selenium is used.

 ## Mailing Feature

 Follow these steps to utilize the mailing feature on the scripts:
 - Go to your google account enable 2 Step Verification
 - Search for App Passwords in Your Account
 - Set the type of application, to Mail and type of device to Windows Computer.
 - Click Generate, replace the password provided in the popup into the script where it says 'EMAIL_PASSWORD'.
 - Change the recipient and senders email address details in the respective places within the script.


## To run in terminal:
- Open Powershell in the local repository folder
- Type:

  ```bash
   python ProductTracker.py
  ```
  or
  ```bash
   python checkstock.py
  ```
