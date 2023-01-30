from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json

# ---------------------------- PASSWORD GENERATOR ------------------------------- #


def search_website():
    web=website_input.get()
    try:
        with open("D:/python/udemy/29_password/d.json","r") as data_file:
            data=json.load(data_file)
          
    except FileNotFoundError:
        messagebox.showinfo(title="Error",message="No Data file found")
    else:
          if web in data:
            email=data[web]["email"]
            pas=data[web]["password"]
            messagebox.showinfo(title=web,message=f"\n Email:{email}\n Password:{pas}")
          else:
              messagebox.showinfo(title="Error",message=f"NO details for the {web} listed")  
                        
            

def password():
    #Password Generator Project
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_list = []

    password_list +=(random.choice(letters) for char in range(nr_letters))
    password_list += (random.choice(symbols) for char in range(nr_symbols))
    password_list += (random.choice(numbers) for char in range(nr_numbers))
    random.shuffle(password_list)

    password="".join(password_list)

    print(f"Your password is: {password}")
    pass_input.insert(0,password)
    pyperclip.copy(password)# to automatically copy the password
          




# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website=website_input.get()
    email=email_input.get()
    password=pass_input.get()
    new_data={
        website:{
            "email":email,
            "password":password
        }
    }
    
    
    #checking for empty inputs
    if len(website)==0 or len(password)==0:
        messagebox.showinfo(title="Oops",message="Please dont leave any fields empty!!!!!")
    else:     
        #message box for confirming the data
        is_ok=messagebox.askokcancel(title=website,message=f"Theses are the details entered \n Email:{email} \n Password:{password}\n Is it oK to save?")
            
        if is_ok:
            try:
                with open("D:/python/udemy/29_password/data.json","r") as data:
                    # json.dump(new_data,data,indent=4)
                    
                    #first reading old data
                    d=json.load(data)
                    #second updating the data
                    d.update(new_data)
            except FileNotFoundError:
                d=new_data        
            finally:    
                with open("D:/python/udemy/29_password/data.json","w") as data:
                    #saving updated data
                    json.dump(d,data,indent=4)
                    website_input.delete(0,END)
                    email_input.delete(0,END)
                    pass_input.delete(0,END)
                    website_input.focus()
    
        

# ---------------------------- UI SETUP ------------------------------- #
window=Tk()
window.title("Password Manager")
window.config(padx=50,pady=50)
# window.minsize(width=500,height=300)


canvas=Canvas(height=200,width=200)
logo_img=PhotoImage(file="D:/python/udemy/29_password/logo.png")
canvas.create_image(100,100,image=logo_img)
canvas.grid(row=0,column=1)

website_label=Label(text="Website:")
website_label.grid(row=1,column=0)
website_input=Entry(width=40)
website_input.grid(row=1,column=1,columnspan=2)
website_input.focus()#for directing the cursor to it
website_button=Button(text="Search",width=10,command=search_website)
website_button.grid(row=1,column=2)


email_label=Label(text="Email/Username:")
email_label.grid(row=2,column=0)
email_input=Entry(width=40)
email_input.grid(row=2,column=1,columnspan=2)
email_input.insert(0,"aniket.gupta20033gmail.com")#END is to used to indicate the last char insert is to precoccupy


pass_label=Label(text="Password:")
pass_label.grid(row=3,column=0)
pass_input=Entry(width=22)
pass_input.grid(row=3,column=1)
btn1=Button(text="Generate Password",width=14,command=password)
btn1.grid(row=3,column=2)

btn2=Button(text="Add",width=36,command=save)
btn2.grid(row=4,column=1,columnspan=2)



window.mainloop()