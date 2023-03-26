# pip install tkinter,pillow,requests
from tkinter import ttk
from tkinter import *
import os, sys
from PIL import Image
from PIL import ImageTk
import json
import requests

def resource_path(relative_path):
    """get absolute path to resource, works for dev and for pyinstaller"""
    try:
        #Pyinstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path,relative_path)

col0 = "#FFFFFF"    #white               
col1 = "#333333"   #black   
col2 = "#E85051"   #red 

window = Tk()
window.geometry("300x400")
window.title("Currency Converter")
window.configure(bg=col0)

#frame
top = Frame(window,width=350,height=60,bg=col2)
top.grid(row=0,column=0)

main = Frame(window,width=350,height=350,bg=col1)
main.grid(row=1,column=0)

def convert():
    import requests

    url = "https://currency-converter18.p.rapidapi.com/api/v1/convert"
    currency_1 = combo1.get()
    currency_2 = combo2.get()
    amount = value.get()

    querystring = {"from":currency_1,"to":currency_2,"amount":amount}
    if currency_2 == "USD":
        Symbol = "$"
    elif currency_2 == "INR":
        Symbol = "₹"
    elif currency_2 == "EUR":
        Symbol = "€"
    elif currency_2 == "CAD":
        Symbol = "CA $"
    elif currency_2 == "BRL":
        Symbol = "R$"
    elif currency_2 == "RUB":
        Symbol = "₽"
    elif currency_2 == "CNY":
        Symbol = "¥"
    elif currency_2 == "AED":
        Symbol = "DH"
    else:
        pass
    headers = {
	    "X-RapidAPI-Key": "b5fec8d484msh8ad6c4a00237110p184398jsn7e2ac701a016",
	    "X-RapidAPI-Host": "currency-converter5.p.rapidapi.com"
    }

    response = requests.request("GET", url, headers=headers, params=querystring)
    data = json.loads(response.text)
    converted_amount = data["result"]["convertedAmount"]
    formatted = Symbol + "{:,.2f}".format(converted_amount)
    result["text"] = formatted 
    print(converted_amount,formatted)


#top frame
icon = Image.open(resource_path("icon.png"))
icon = icon.resize((40,40))
icon = ImageTk.PhotoImage(icon)
app_name = Label(top,image=icon,compound=LEFT,text="Currency Converter",height=5,padx=10,pady=25,anchor=CENTER,font="Times 18 bold",bg=col2,fg=col0)
app_name.place(x=0,y=0)

#main frame
result = Label(main,text=" ",width=16,height=2,pady=7,relief="solid",anchor=CENTER,font="Ivy 15 bold",bg=col0,fg=col1 )
result.place(x=58,y=10)

currency = ["INR","USD","EUR","CAD","BRL","RUB","CNY","AED"]

FROM_LABEL= Label(main,text="From",width=8,height=1,pady=0,padx=0,relief="flat",anchor=NW,font="Ivy 13 bold",bg=col1,fg=col0)
FROM_LABEL.place(x=36,y=90)
combo1 = ttk.Combobox(main,width=8,justify=CENTER,font=("Ivy 12 bold"))
combo1["values"]=(currency)
combo1.place(x=45,y=115)

To_LABEL= Label(main,text="To",width=7,height=1,pady=0,padx=0,relief="flat",anchor=NW,font="Ivy 13 bold",bg=col1,fg=col0)
To_LABEL.place(x=151,y=90)
combo2 = ttk.Combobox(main,width=8,justify=CENTER,font=("Ivy 12 bold"))
combo2["values"]=(currency)
combo2.place(x=165,y=115)

value=Entry(main,width=22,justify=CENTER,font=("Ivy 12 bold"),relief=SOLID)
value.place(x=55,y=165)

button = Button(main,text="Converter",width=19,padx=5,height=1,bg=col2,fg=col0,font=("Ivy 12 bold"),command=convert)
button.place(x=53,y=210)
window.mainloop()