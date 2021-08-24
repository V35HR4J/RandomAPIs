import re,pytz,requests,bs4,time
from datetime import datetime
from nepali_date import NepaliDate
def td():
  d_request = requests.get('https://english.hamropatro.com/')
  soup = bs4.BeautifulSoup(d_request.text, "html.parser")
  alll = soup.find_all('div', {'class' : re.compile('events')})
  for i in alll:
    items = ' '.join(i.text.split())
  #nps = ''.join([str(elem) for elem in item])
  date_BS = NepaliDate.today()
  date_BSN = NepaliDate.today(lang='nep')
  tz_NP = pytz.timezone('Asia/Kathmandu')
  datetime_NP = datetime.now(tz_NP)
  nptime = datetime_NP.strftime("%I:%M %p")
  npday = datetime_NP.strftime("%A")
  npdate = datetime_NP.strftime("%b %d %Y")
  npdt = '{0:B} {0:d}, {0:Y}'.format(date_BS)
  datetimee = f"   [ TIMEDATE ]    \n🕒 {nptime}, {npday}\n📅 {npdate}\n🇳🇵 {npdt}\n📄 {items}"
  return datetimee

##print(td())
