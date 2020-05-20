import time, re
from bs4 import BeautifulSoup
from selenium import webdriver



#URL = ''
URL = input('input your youtube playlist URL: ')
driver = webdriver.Chrome()
driver.get(URL)
time.sleep(2)
day, hour, minuate, second = 0, 0, 0, 0
time_re = re.compile('([0-9]*):([0-9]*)')
soup = BeautifulSoup(driver.page_source, 'html.parser')
Allvideos = soup.findAll('span', {'class':'style-scope ytd-thumbnail-overlay-time-status-renderer'})
for i in Allvideos:
    minuate += int(time_re.search(i.string.strip()).group(1))
    second += int(time_re.search(i.string.strip()).group(2))

minuate += second//60
second = second%60
hour += minuate//60
minuate = minuate%60
day += hour//24
hour = hour%24

print('total length of playlist videos is {}d {}h {}m {}s.'.format(day, hour, minuate, second))
