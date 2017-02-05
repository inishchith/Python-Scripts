# SmsBot :scroll:

### A Python Module to send Sms to any Number in India using [Way2Sms](http://site23.way2sms.com/content/index.html).

**Features**
  > Send Upto 100 Daily Sms.
  > Delivered under 10 seconds .
  > Maximum length 139 characters .
  > You can also send Group SMS to many friends in one go .

**Usage** 
>You can take a look at [Demo](https://github.com/inishchith/Python-Scripts-Projects/blob/master/SmsBot/Test.py) Or 
```python
import SmsBot
query = SmsBot.sms("username","password") # username is usually Mobile Number (Logging in)
my_message=input("Enter Your Message")
query.send("recipient",my_message) # recipient = receiver's numebr
query.Logout()
```

**list Of External Modules and their installation**
>BeautifulSoup 
  ```sh
  #python3
  $ pip3 install BeautiifulSoup4
  ```
>Requests 
  ```sh
  $ pip3 install requests
  ```
**Note-** SmsBot.py Should be in your directory 
