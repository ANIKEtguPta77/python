import requests
import datetime as dt
import smtplib

my_email="qh182756@gmail.com"
password="uywgriiyqjcaauyg"




def is_iss_overhead():
    #without paramaters api
    response=requests.get(url="http://api.open-notify.org/iss-now.json")
    print(response.status_code)

    # if response.status_code==404:
    #     raise Exception("That response doesnt exist")
    # else:
    #     raise Exception("You are not authorised to access the data")

    response.raise_for_status()#if api is not successful then will show error

    # #STATUS CODE MEANING
    # # 1XX-WE are loading
    # # 2XX- here you go with the Data
    # # 3XX-GO away
    # # 4XX-ERROR(You screwed up-you did mistake)
    # # 5XX-i screwed up-server did a mistake

    longitude=float(response.json()["iss_position"]["longitude"])
    latitude=float(response.json()["iss_position"]["latitude"])


    if 15<=latitude<=26 and 65<=longitude<=77:
        return True



def is_night():

    #with parameters api

    parameters={
        "lat":21.705135,
        "lng":72.995872,
        "formatted":0,    
    }


    response=requests.get(url="https://api.sunrise-sunset.org/json",params=parameters)
    response.raise_for_status()
    #print(response.status_code)
    data=response.json()

    now=dt.datetime.now()
    

    sunset=int(data["results"]["sunset"].split("T")[1].split(":")[0])
    sunrise=int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    if now.hour>=sunset or now.hour<sunrise:
        return True
        
        
if is_night() and is_iss_overhead():
    with smtplib.SMTP("smtp.gmail.com") as connection:

        connection.starttls()#to make the message encrypted so that people in between cant read it
        connection.login(user=my_email,password=password)
        connection.sendmail(from_addr=my_email,to_addrs="aniket.gupta20033@gmail.com",msg="Subject:Look UP\n\nIss is just above you")