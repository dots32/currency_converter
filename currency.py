import requests
from bs4 import BeautifulSoup

fromEURL = "https://www.google.com/finance/quote/EUR-USD"
toEURL = "https://www.google.com/finance/quote/USD-EUR"
fromBURL = "https://www.google.com/finance/quote/BGN-USD"
toBURL = "https://www.google.com/finance/quote/USD-BGN"
fromCAURL = "https://www.google.com/finance/quote/CAD-USD"
toCAURL = "https://www.google.com/finance/quote/USD-CAD"
fromCHURL = "https://www.google.com/finance/quote/CNY-USD"
toCHURL = "https://www.google.com/finance/quote/USD-CNY"
fromCZURL = "https://www.google.com/finance/quote/CZK-USD"
toCZURL = "https://www.google.com/finance/quote/USD-CZK"
fromDURL = "https://www.google.com/finance/quote/DKK-USD"
toDURL = "https://www.google.com/finance/quote/USD-DKK"
fromHURL = "https://www.google.com/finance/quote/HUF-USD"
toHURL = "https://www.google.com/finance/quote/USD-HUF"
fromJURL = "https://www.google.com/finance/quote/JPY-USD"
toJURL = "https://www.google.com/finance/quote/USD-JPY"
fromNURL = "https://www.google.com/finance/quote/ANG-USD"
toNURL = "https://www.google.com/finance/quote/USD-ANG"
fromPURL = "https://www.google.com/finance/quote/PLN-USD"
toPURL = "https://www.google.com/finance/quote/USD-PLN"
fromROURL = "https://www.google.com/finance/quote/RON-USD"
toROURL = "https://www.google.com/finance/quote/USD-RON"
fromRUURL = "https://www.google.com/finance/quote/RUB-USD"
toRUURL = "https://www.google.com/finance/quote/USD-RUB"
fromSEURL = "https://www.google.com/finance/quote/SEK-USD"
toSEURL = "https://www.google.com/finance/quote/USD-SEK"
fromSIURL = "https://www.google.com/finance/quote/CHF-USD"
toSIURL = "https://www.google.com/finance/quote/USD-CHF"

print("welcome to the currency converter!")
From = input("What currency will you be converting from? (3-Letter code)")
Amount = input(f"How many {From} do you have?")
To = input("What currency will you be converting to?")
try:
    fromEfortt = requests.get(url=fromEURL)
    fromEfort = fromEfortt.text
    fromEsoup = BeautifulSoup(fromEfort, "html.parser")
    fromEstuff = fromEsoup.find(class_="YMlKec fxKbKc")
    fromE = str(fromEstuff).split(">")[1].split("<")[0]

    toEfortt = requests.get(url=toEURL)
    toEfort = toEfortt.text
    toEsoup = BeautifulSoup(toEfort, "html.parser")
    toEstuff = toEsoup.find(class_="YMlKec fxKbKc")
    toE = str(toEstuff).split(">")[1].split("<")[0]

    fromBfortt = requests.get(url=fromBURL)
    fromBfort = fromBfortt.text
    fromBsoup = BeautifulSoup(fromBfort, "html.parser")
    fromBstuff = fromBsoup.find(class_="YMlKec fxKbKc")
    fromB = str(fromBstuff).split(">")[1].split("<")[0]

    toBfortt = requests.get(url=toBURL)
    toBfort = toBfortt.text
    toBsoup = BeautifulSoup(toBfort, "html.parser")
    toBstuff = toBsoup.find(class_="YMlKec fxKbKc")
    toB = str(toBstuff).split(">")[1].split("<")[0]

    fromCAfortt = requests.get(url=fromCAURL)
    fromCAfort = fromCAfortt.text
    fromCAsoup = BeautifulSoup(fromCAfort, "html.parser")
    fromCAstuff = fromCAsoup.find(class_="YMlKec fxKbKc")
    fromCA = str(fromCAstuff).split(">")[1].split("<")[0]

    toCAfortt = requests.get(url=toCAURL)
    toCAfort = toCAfortt.text
    toCAsoup = BeautifulSoup(toCAfort, "html.parser")
    toCAstuff = toCAsoup.find(class_="YMlKec fxKbKc")
    toCA = str(toCAstuff).split(">")[1].split("<")[0]

    fromCHfortt = requests.get(url=fromCHURL)
    fromCHfort = fromCHfortt.text
    fromCHsoup = BeautifulSoup(fromCHfort, "html.parser")
    fromCHstuff = fromCHsoup.find(class_="YMlKec fxKbKc")
    fromCH = str(fromCHstuff).split(">")[1].split("<")[0]

    toCHfortt = requests.get(url=toCHURL)
    toCHfort = toCHfortt.text
    toCHsoup = BeautifulSoup(toCHfort, "html.parser")
    toCHstuff = toCHsoup.find(class_="YMlKec fxKbKc")
    toCH = str(toCHstuff).split(">")[1].split("<")[0]

    fromCZfortt = requests.get(url=fromCZURL)
    fromCZfort = fromCZfortt.text
    fromCZsoup = BeautifulSoup(fromCZfort, "html.parser")
    fromCZstuff = fromCZsoup.find(class_="YMlKec fxKbKc")
    fromCZ = str(fromCZstuff).split(">")[1].split("<")[0]

    toCZfortt = requests.get(url=toCZURL)
    toCZfort = toCZfortt.text
    toCZsoup = BeautifulSoup(toCZfort, "html.parser")
    toCZstuff = toCZsoup.find(class_="YMlKec fxKbKc")
    toCZ = str(toCZstuff).split(">")[1].split("<")[0]

    fromDfortt = requests.get(url=fromDURL)
    fromDfort = fromDfortt.text
    fromDsoup = BeautifulSoup(fromDfort, "html.parser")
    fromDstuff = fromDsoup.find(class_="YMlKec fxKbKc")
    fromD = str(fromDstuff).split(">")[1].split("<")[0]

    toDfortt = requests.get(url=toDURL)
    toDfort = toDfortt.text
    toDsoup = BeautifulSoup(toDfort, "html.parser")
    toDstuff = toDsoup.find(class_="YMlKec fxKbKc")
    toD = str(toDstuff).split(">")[1].split("<")[0]

    fromHfortt = requests.get(url=fromHURL)
    fromHfort = fromHfortt.text
    fromHsoup = BeautifulSoup(fromHfort, "html.parser")
    fromHstuff = fromHsoup.find(class_="YMlKec fxKbKc")
    fromH = str(fromHstuff).split(">")[1].split("<")[0]

    toHfortt = requests.get(url=toHURL)
    toHfort = toHfortt.text
    toHsoup = BeautifulSoup(toHfort, "html.parser")
    toHstuff = toHsoup.find(class_="YMlKec fxKbKc")
    toH = str(toHstuff).split(">")[1].split("<")[0]

    fromJfortt = requests.get(url=fromJURL)
    fromJfort = fromJfortt.text
    fromJsoup = BeautifulSoup(fromJfort, "html.parser")
    fromJstuff = fromJsoup.find(class_="YMlKec fxKbKc")
    fromJ = str(fromJstuff).split(">")[1].split("<")[0]

    toJfortt = requests.get(url=toJURL)
    toJfort = toJfortt.text
    toJsoup = BeautifulSoup(toJfort, "html.parser")
    toJstuff = toJsoup.find(class_="YMlKec fxKbKc")
    toJ = str(toJstuff).split(">")[1].split("<")[0]

    fromNfortt = requests.get(url=fromNURL)
    fromNfort = fromNfortt.text
    fromNsoup = BeautifulSoup(fromNfort, "html.parser")
    fromNstuff = fromNsoup.find(class_="YMlKec fxKbKc")
    fromN = str(fromNstuff).split(">")[1].split("<")[0]

    toNfortt = requests.get(url=toNURL)
    toNfort = toNfortt.text
    toNsoup = BeautifulSoup(toNfort, "html.parser")
    toNstuff = toNsoup.find(class_="YMlKec fxKbKc")
    toN = str(toNstuff).split(">")[1].split("<")[0]

    fromPfortt = requests.get(url=fromPURL)
    fromPfort = fromPfortt.text
    fromPsoup = BeautifulSoup(fromPfort, "html.parser")
    fromPstuff = fromPsoup.find(class_="YMlKec fxKbKc")
    fromP = str(fromPstuff).split(">")[1].split("<")[0]

    toPfortt = requests.get(url=toPURL)
    toPfort = toPfortt.text
    toPsoup = BeautifulSoup(toPfort, "html.parser")
    toPstuff = toPsoup.find(class_="YMlKec fxKbKc")
    toP = str(toPstuff).split(">")[1].split("<")[0]

    fromROfortt = requests.get(url=fromROURL)
    fromROfort = fromROfortt.text
    fromROsoup = BeautifulSoup(fromROfort, "html.parser")
    fromROstuff = fromROsoup.find(class_="YMlKec fxKbKc")
    fromRO = str(fromROstuff).split(">")[1].split("<")[0]

    toROfortt = requests.get(url=toROURL)
    toROfort = toROfortt.text
    toROsoup = BeautifulSoup(toROfort, "html.parser")
    toROstuff = toROsoup.find(class_="YMlKec fxKbKc")
    toRO = str(toROstuff).split(">")[1].split("<")[0]

    fromRUfortt = requests.get(url=fromRUURL)
    fromRUfort = fromRUfortt.text
    fromRUsoup = BeautifulSoup(fromRUfort, "html.parser")
    fromRUstuff = fromRUsoup.find(class_="YMlKec fxKbKc")
    fromRU = str(fromRUstuff).split(">")[1].split("<")[0]

    toRUfortt = requests.get(url=toRUURL)
    toRUfort = toRUfortt.text
    toRUsoup = BeautifulSoup(toRUfort, "html.parser")
    toRUstuff = toRUsoup.find(class_="YMlKec fxKbKc")
    toRU = str(toRUstuff).split(">")[1].split("<")[0]

    fromSEfortt = requests.get(url=fromSEURL)
    fromSEfort = fromSEfortt.text
    fromSEsoup = BeautifulSoup(fromSEfort, "html.parser")
    fromSEstuff = fromSEsoup.find(class_="YMlKec fxKbKc")
    fromSE = str(fromSEstuff).split(">")[1].split("<")[0]

    toSEfortt = requests.get(url=toSEURL)
    toSEfort = toSEfortt.text
    toSEsoup = BeautifulSoup(toSEfort, "html.parser")
    toSEstuff = toSEsoup.find(class_="YMlKec fxKbKc")
    toSE = str(toSEstuff).split(">")[1].split("<")[0]

    fromSIfortt = requests.get(url=fromSIURL)
    fromSIfort = fromSIfortt.text
    fromSIsoup = BeautifulSoup(fromSIfort, "html.parser")
    fromSIstuff = fromSIsoup.find(class_="YMlKec fxKbKc")
    fromSI = str(fromSIstuff).split(">")[1].split("<")[0]

    toSIfortt = requests.get(url=toSIURL)
    toSIfort = toSIfortt.text
    toSIsoup = BeautifulSoup(toSIfort, "html.parser")
    toSIstuff = toSIsoup.find(class_="YMlKec fxKbKc")
    toSI = str(toSIstuff).split(">")[1].split("<")[0]
except:
    print("error bro shit sad on granathon")
finally:
    currencies = {
        # "fromEUR": float(fromE),
        "toEUR": float(toE),
        "fromBGN": float(fromB),
        "toBGN": float(toB),
        "fromCAD": float(fromCA),
        "toCAD": float(toCA),
        "fromCNY": float(fromCH),
        "toCNY": float(toCH),
        "fromCZK": float(fromCZ),
        "toCZK": float(toCZ),
        "fromDKK": float(fromD),
        "toDKK": float(toD),
        "fromHUF": float(fromH),
        "toHUF": float(toH),
        "fromJPY": float(fromJ),
        "toJPY": float(toJ),
        "fromANG": float(fromN),
        "toANG": float(toN),
        "fromPLN": float(fromP),
        "toPLN": float(toP),
        "fromRON": float(fromRO),
        "toRON": float(toRO),
        "fromRUB": float(fromRU),
        "toRUB": float(toRU),
        "fromSEK": float(fromSE),
        "toSEK": float(toSE),
        "fromCHF": float(fromSI),
        "toCHF": float(toSI)
    }
    curfrom = currencies.get(f"from{From}")
    curto = currencies.get(f"to{To}")
    def convert():
        FromToUs = (curfrom * float(Amount))
        FromToUsToTo = (FromToUs * curto)
        return FromToUsToTo
    print(convert())








