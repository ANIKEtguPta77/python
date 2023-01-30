import smtplib
my_email="qh182756@gmail.com"
password="uywgriiyqjcaauyg"
with smtplib.SMTP("smtp.gmail.com",port=587) as connection:

    connection.starttls()#to make the message encrypted so that people in between cant read it
    connection.login(user=my_email,password=password)
    connection.sendmail(from_addr=my_email,to_addrs="aniket.gupta20033@gmail.com",msg="Subject:Hello\n\nThis is my body")
    