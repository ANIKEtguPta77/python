import smtplib
import pandas
import datetime as dt
import random 

my_email="qh182756@gmail.com"
password="uywgriiyqjcaauyg"


# data=pandas.read_csv("D:/python/udemy/32-Emailsmtp_datetimemodule/birthdays.csv")
data=pandas.read_csv("birthdays.csv")
data_dic={(row_data["month"],row_data["day"]):row_data for (index,row_data) in data.iterrows()}

now=dt.datetime.now()

if (now.month,now.day) in data_dic:
    number=random.randint(1,3)
    with open(f"letter_templates/letter_{number}.txt") as t:
        text1=t.read()
        text1=text1.replace("[NAME]",data_dic[(now.month,now.day)]["name"])
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()#to make the message encrypted so that people in between cant read it
        connection.login(user=my_email,password=password)
        connection.sendmail(from_addr=my_email,to_addrs=data_dic[((now.month,now.day))]["email"],msg=f"Subject:Birthday Wishes\n\n{text1}")



