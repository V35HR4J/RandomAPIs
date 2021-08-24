import requests
from bs4 import BeautifulSoup

#Scraper Function
def scrape(rows,i):
    try:
        head = rows[i].find('th').text.strip()
        head = " ".join(head.split())
    except:
        head = '-'
    try:
        data = rows[i].find('td').text.strip()
        data = " ".join(data.split())
    except:
        data = '-'
    row = f"{head}: {data}\n"
    return row

#Main API
def getstats(symbol):
    url = f"https://merolagani.com/CompanyDetail.aspx?symbol={symbol.upper()}"
    try:
        result = requests.get(url)
        soup = BeautifulSoup(result.text,"html.parser")
        final = f"{soup.find('h4').text.strip()}\n"
        if len(final.strip())==0:
            return "Could not find any result for this symbol!\nPlease Check the Symbol and Try Again!"
    except:
        return "There was some unknown error! Please try again!"
    rows = soup.find_all('tr')
    for i in range(13):
        final += scrape(rows,i)
    for i in range(len(rows)-8,len(rows)-6):
        final += scrape(rows,i)
    return final.strip()
