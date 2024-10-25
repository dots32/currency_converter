from operator import truediv

import requests
from bs4 import BeautifulSoup
from tkinter import *



window = Tk()

URL = "https://www.x-rates.com/table/?from=USD&amount=1"
BG = "#f7f5dd"
PFONT = ('courier', 18, 'bold')
TFONT = ('courier', 18, 'bold')
FONT = ('courier', 10, 'bold')

fortt = requests.get(url=URL)
fort = fortt.text

soup = BeautifulSoup(fort, "html.parser")
soupstuff = soup.findAll(class_="rtRates")
curog = []
cur = []
for thing in soupstuff:
    curog.append(thing)
for thingy in curog:
    toandfromusd = str(thingy).split(">")[2].split("<")[0]
    cur.append(toandfromusd)
for value in range(0, 20):
    cur.pop(0)
tocur = []
fromcur = []
for forty in cur:
    if cur.index(forty) % 2 != 0:
        tocur.append(forty)
    elif cur.index(forty) % 2 == 0:
        fromcur.append(forty)

AVAILABLECURRENCIESF= ['Argentine Peso ', 'Australian Dollar', 'Bahraini Dinar', 'Botswana Pula', 'Brazilian Real', 'British Pound', 'Bruneian Dollar', 'Bulgarian Lev', 'Canadian Dollar', 'Chilean Peso', 'Chinese Yuan Renminbi', 'Colombian Peso', 'Czech Koruna', 'Danish Krone', 'Emirati Dirham', 'Euro', 'Hong Kong Dollar', 'Hungarian Forint', 'Icelandic Krona', 'Indian Rupee', 'Indonesian Rupiah', 'Iranian Rial', 'Israeli Shekel', 'Japanese Yen', 'Kazakhstani Tenge', 'Kuwaiti Dinar', 'Libyan Dinar', 'Malaysian Ringgit', 'Mauritian Rupee', 'Mexican Peso', 'Nepalese Rupee', 'New Zealand Dollar', 'Norwegian Krone', 'Omani Rial', 'Pakistani Rupee', 'Philippine Peso', 'Polish Zloty', 'Qatari Riyal', 'Romanian New Leu', 'Russian Ruble', 'Saudi Arabian Riyal', 'Singapore Dollar', 'South African Rand', 'South Korean Won', 'Sri Lankan Rupee', 'Swedish Krona', 'Swiss Franc', 'Taiwan New Dollar', 'Thai Baht', 'Trinidadian Dollar', 'Turkish Lira', 'Venezuelan Bolivar']
AVAILABLECURRENCIES = ['ARS','AUD','BHD','BWP','BRL','BND','BGN','CAD','CLP','CNY','COP','CZK','DKK','EUR','HKD','HUF','ISK','INR','IDP','IRR','ILS','JPY','KZT','KRW','KWD','LYD','MYR','MUR','MXN','NPR','NZD','NOK','OMR','PKR','PHP','PLN','QAR','RON','RUB','SAR','SGD','ZAR','LKR','SEK','CHF','TWD','GBP','TTD','TRY','AED','BGP','VED']

fromcurrencyavailable = False
isanumber = False
tocurrencyavailable = False
seelist = False

tocont = dict(zip(AVAILABLECURRENCIES, fromcur))
fromcont = dict(zip(AVAILABLECURRENCIES, tocur))

window.title('currency converter')
window.minsize(width=200, height=250)
window.config(bg=BG, padx=70, pady=70)

greet = Label(text='welcome to the currency converter!', font=TFONT, bg=BG)
greet.grid(column=1, row=0)

fromlabel = Label(text='Type the currency you will be converting from:', font=FONT, bg=BG)
fromlabel.place(x=0, y=40)

frombox = Entry(width=10, bg=BG)
frombox.focus()
frombox.insert(END, 'ex: USD')
frombox.place(x=375, y=42)

amountlabel = Label(text=f'How much of this currency do you have', font=FONT, bg=BG)
amountlabel.place(x=0, y=60)

amountbox = Entry(width=10, bg=BG)
amountbox.insert(END, 'ex: 10')
amountbox.place(x=375, y=62)

tolabel = Label(text='Type the currency you will be converting to:', font=FONT, bg=BG)
tolabel.place(x=0, y=80)

tobox = Entry(width=10, bg=BG)
tobox.insert(END, 'ex: PLN')
tobox.place(x=375, y=82)

def checkfrom():
    fromget = frombox.get()
    if fromget.upper() not in AVAILABLECURRENCIES:
        frombox.delete(0, END)
        frombox.insert(END, 'N/A')
        return False
    else:
        return True
def checkamount():
    amountget = amountbox.get()
    try:
        int(amountget)
    except ValueError:
        amountbox.delete(0, END)
        amountbox.insert(END, 'N/A')
        return False
    else:
        return True
def checkto():
    toget = tobox.get()
    if toget.upper() not in AVAILABLECURRENCIES:
        tobox.delete(0, END)
        tobox.insert(END, 'N/A')
        return False
    else:
        return True
def doitall():
    checkfrom()
    checkamount()
    checkto()
    if not checkfrom() or not checkamount() or not checkto():
        return False
    elif checkfrom() and checkamount() and checkto():
        return True

def convert():
    fromget = frombox.get()
    amountget = amountbox.get()
    toget = tobox.get()
    if not doitall():
        return False
    elif doitall():
        curfrom = fromcont.get(f"{fromget.upper()}")
        curto = tocont.get(f"{toget.upper()}")
        FromToUs = (float(curfrom) * float(amountget))
        FromToUsToTo = (FromToUs * float(curto))
        return round(FromToUsToTo, 3)

def createconvlabel():
    convert()
    if not convert():
        pass
    else:
        convlabel = Label(text=f'{convert()}', font=TFONT, bg=BG)
        convlabel.place(x=185, y=135)



convertb = Button(text='Convert', bg=BG, width=25, highlightthickness=0, command=createconvlabel)
convertb.place(x=140, y=105)


window.mainloop()


while not seelist:
    seeavcur = input("Would you like to see the available currencies for conversion? (Y/N)")
    if seeavcur.upper() == "Y":
        print(AVAILABLECURRENCIESF)
    elif seeavcur.upper() == "N":
        seelist = True
    elif not seeavcur.upper() == "Y" or not seeavcur.upper() == "N":
        print("Not a valid response. Please ensure that your answer is in Y/N format.")




