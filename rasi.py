import requests
import bs4
def rasifal(rasi):
  khojeko = requests.get(f'https://www.hamropatro.com/rashifal/daily/{rasi}')
  arko_khoj = bs4.BeautifulSoup(khojeko.text, "html.parser")
  arkoo_khoj = arko_khoj.find_all('p')[0].find_all(text=True, recursive=True)
  hehe_rasi = ''.join([str(elem) for elem in arkoo_khoj])
  final_rasi = f'{hehe_rasi}'
  return final_rasi
  
##print(rasi('dhanu'))
