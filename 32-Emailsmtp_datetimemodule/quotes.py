import datetime as dt
from random import choice
import smtplib

my_email="qh182756@gmail.com"
password="uywgriiyqjcaauyg"
 
now=dt.datetime.now()    
current_day=now.weekday()
if current_day==2:
    with open("D:/python/udemy/32-Emailsmtp_datetimemodule/quotes.txt") as data:
        lines=data.readlines()
        quote=choice(lines)
    print(quote)
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()#to make the message encrypted so that people in between cant read it
        connection.login(user=my_email,password=password)
        connection.sendmail(from_addr=my_email,to_addrs="aniket.gupta20033@gmail.com",msg=f"Subject:Monday motivation\n\n{quote}")
        
        