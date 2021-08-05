from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
# import pandas as pd
import time

driver = webdriver.Firefox()
driver.get('https://www.airbnb.fr/rooms/14779219?adults=1&source_impression_id=p3_1624967210_9AOeCV7QEe%2B9foPD&guests=1')

time.sleep(10)
title = driver.find_element_by_xpath('//*[@id="site-content"]/div/div[1]/div[1]/div[1]/div/div/div/div/section/div[1]/span/h1').text

subtitle = driver.find_element_by_xpath('//*[@id="site-content"]/div/div[1]/div[3]/div/div[1]/div/div/div[1]/div/div/section/div/div/div/div[1]/div[1]/h2').text
subinfo1 = driver.find_element_by_xpath('//*[@id="site-content"]/div/div[1]/div[3]/div/div[1]/div/div/div[1]/div/div/section/div/div/div/div[1]/div[2]/span[1]').text
subinfo2 = driver.find_element_by_xpath('//*[@id="site-content"]/div/div[1]/div[3]/div/div[1]/div/div/div[1]/div/div/section/div/div/div/div[1]/div[2]/span[4]').text
subinfo3 = driver.find_element_by_xpath('//*[@id="site-content"]/div/div[1]/div[3]/div/div[1]/div/div/div[1]/div/div/section/div/div/div/div[1]/div[2]/span[7]').text
subinfo4 = driver.find_element_by_xpath('//*[@id="site-content"]/div/div[1]/div[3]/div/div[1]/div/div/div[1]/div/div/section/div/div/div/div[1]/div[2]/span[10]').text
accdiv = driver.find_element_by_xpath('//*[@id="site-content"]/div/div[1]/div[3]/div/div[1]/div/div/div[4]/div/div[2]/section/div[3]').text
print(title)
print(subtitle)
print(subinfo1)
print(subinfo2)
print(subinfo3)
print(subinfo4)
print(accdiv)