from selenium import webdriver
from selenium.webdriver.common.keys import Keys
# from bs4 import BeautifulSoup


driver = webdriver.Chrome('./chromedriver')
driver.get('https://datalab.naver.com/keyword/realtimeList.naver?where=main')

keywords = driver.find_elements_by_css_selector('#content > div > div.keyword_carousel > div > div > div:nth-child(1) > div > div > ul')

texts = [keyword.text for keyword in keywords]

print('네이버 실시간 검색어')
with open('result.txt', 'w', encoding='utf-8') as f:
    for text in texts:
        f.write(text+'\n')

driver.quit()

print(texts)