import requests
from bs4 import BeautifulSoup
from pprint import PrettyPrinter, pprint

URL = "https://www.x-rates.com/table/?from=USD&amount=1"

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
print("welcome to the currency converter!")
fromcurrencyavailable = False
isanumber = False
tocurrencyavailable = False
seelist = False
while not seelist:
    seeavcur = input("Would you like to see the available currencies for conversion? (Y/N)")
    if seeavcur.upper() == "Y":
        print(AVAILABLECURRENCIESF)
    elif seeavcur.upper() == "N":
        seelist = True
    elif not seeavcur.upper() == "Y" or not seeavcur.upper() == "Y":
        print("Not a valid response. Please ensure that your answer is in Y/N format.")

while not fromcurrencyavailable:
    FROM = input("What currency will you be converting from? (3-Letter code)")
    if FROM.upper() not in AVAILABLECURRENCIES:
        print("This currency is not available for conversion, or is not a currency. PLease try a different currency.")
    elif FROM.upper() in AVAILABLECURRENCIES:
        fromcurrencyavailable = True

while not isanumber:
    Amount = input(f"How many {FROM.upper()} do you have?")
    try:
        int(Amount)
    except ValueError:
        print("Not a number or not in valid format")
    else:
        isanumber = True

while not tocurrencyavailable:
    TO = input("What currency will you be converting to?")
    if TO.upper() not in AVAILABLECURRENCIES:
        print("This currency is not available for conversion, or is not a currency. PLease try a different currency.")
    elif TO.upper() in AVAILABLECURRENCIES:
        tocurrencyavailable = True


tocont = dict(zip(AVAILABLECURRENCIES, fromcur))
fromcont = dict(zip(AVAILABLECURRENCIES, tocur))

curfrom = fromcont.get(f"{FROM.upper()}")
curto = tocont.get(f"{TO.upper()}")
print(curfrom, curto)
print(tocont, fromcont)
def convert():
    FromToUs = (float(curfrom) * float(Amount))
    FromToUsToTo = (FromToUs * float(curto))
    return FromToUsToTo
print(convert())