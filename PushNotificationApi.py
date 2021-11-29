import time
import schedule
import requests as requests
from win10toast_click import ToastNotifier
import webbrowser
# functions 
page_url = 'https://smarttrader.io/'
def open_url():
    try: 
        webbrowser.open_new(page_url)
    except: 
        print('Failed to open URL. Unsupported variable type.')


def notification(message): # showcase
    toaster = ToastNotifier()# initialize 
    toaster.show_toast(
        "Stock Exchange", # title
        message, # message 
        icon_path=None, # 'icon_path' 
        duration=3, # for how many seconds toast should be visible; None = leave notification in Notification Center
        threaded=False, # True = run other code in parallel; False = code execution will wait till notification disappears 
        callback_on_click=open_url # click notification to run function 
    )
#API
def stockExchange():
    header = {'Connection': 'keep-alive',
                    'Expires': '-1',
                    'Upgrade-Insecure-Requests': '1',
                    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) \
                    AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36'
                    } #Añadimos Headers para poder permitir el request en el server

    url = 'https://query1.finance.yahoo.com/v6/finance/quote?symbols=^N225,^DAX-EU,^IXIC'
    response = requests.get(url, headers=header) 
    data = response.json() #Parseamos la información para poder leerla como un Json(objeto clave, valor) 
    list = data['quoteResponse']['result']
    for info in list: # Using for loop
        regularMarketChangePercent = info['regularMarketChangePercent']
        companyName=info['shortName']
        if regularMarketChangePercent > 0.5:
            notification(companyName + "Stock Exchange rose")
            print(regularMarketChangePercent)
        elif regularMarketChangePercent < -0.5:
            notification(companyName + "Stock Exchange fell")
            print(regularMarketChangePercent)
schedule.every(10).seconds.do(stockExchange)       
while(True):
    schedule.run_pending()        
    time.sleep(1)



