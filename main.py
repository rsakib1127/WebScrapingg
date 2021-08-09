from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options
from bs4 import BeautifulSoup
import time
import airtable
import json
f = open('airtable.json',)
data = json.load(f)

at = airtable.Airtable(data['BaseID'],data['Table'],data['APIkey'])

options = Options()
options.headless = True


try:
    driver = webdriver.Firefox(options=options)
except:
    driver = webdriver.Firefox(options=options, executable_path="/usr/local/bin/geckodriver")
    pass

url = input("Enter URL: ")
driver.get(url)

time.sleep(10)
try:
    title = driver.find_element_by_xpath(
        '//*[@id="site-content"]/div/div[1]/div[1]/div[1]/div/div/div/div/section/div[1]/span/h1').text

except:
    title = ''
    pass

try:
    address = driver.find_element_by_class_name('_1qdp1ym').text
    address = address.replace("\n", " ")
    address_trim = address.split('·')[-1].replace(" Partager Enregistrer", '')
    print(address_trim)
except:
    address_trim = ''
    pass


try:
    subtitle = driver.find_element_by_xpath(
        '//*[@id="site-content"]/div/div[1]/div[3]/div/div[1]/div/div/div[1]/div/div/section/div/div/div/div[1]/div[1]/h2').text

except:
    pass


try:
    capacite = driver.find_element_by_xpath(
        '//*[@id="site-content"]/div/div[1]/div[3]/div/div[1]/div/div/div[1]/div/div/section/div/div/div/div[1]/div[2]/span[1]').text

    print(int(capacite.split(' ')[0]))
    capacite_int = int(capacite.split(' ')[0])
except:
    capacite_int = 0
    pass



try:
    chambre = driver.find_element_by_xpath(
        '//*[@id="site-content"]/div/div[1]/div[3]/div/div[1]/div/div/div[1]/div/div/section/div/div/div/div[1]/div[2]/span[4]').text
    print(int(chambre.split(' ')[0]))
    chambre_int = int(chambre.split(' ')[0])
except:
    chambre_int = 0
    pass


try:
    lits = driver.find_element_by_xpath(
        '//*[@id="site-content"]/div/div[1]/div[3]/div/div[1]/div/div/div[1]/div/div/section/div/div/div/div[1]/div[2]/span[7]').text

except:
    lits = 0
    pass


try:
    salles_de_bain = driver.find_element_by_xpath(
        '//*[@id="site-content"]/div/div[1]/div[3]/div/div[1]/div/div/div[1]/div/div/section/div/div/div/div[1]/div[2]/span[10]').text
    print(int(salles_de_bain.split(' ')[0]))
    salles_de_bain_int = int(salles_de_bain.split(' ')[0])
except:
    salles_de_bain_int = 0
    pass
# address = driver.find_element_by_xpath('//*[@id="site-content"]/div/div[1]/div[1]/div[1]/div/div/div/div/section/div[2]/div[1]/span[3]/button/span').text



try:
    type_de_chambre = driver.find_element_by_xpath(
        '//*[@id="site-content"]/div/div[1]/div[3]/div/div[1]/div/div/div[2]/div/div[2]/div[1]/div[2]/div[1]').text
except:
    type_de_chambre = ''
    pass



try:
    type_de_logement = driver.find_element_by_xpath(
        '//*[@id="site-content"]/div/div[1]/div[3]/div/div[1]/div/div/div[2]/div/div[2]/div[1]/div[2]/div[2]').text

except:
    type_de_logement = ''
    pass
#marche =

print(title)
print('\"'+address+'\"')
print(subtitle)



print(lits)

print(address)
print(type_de_chambre)
print(type_de_logement)

chambre_type = 'Logement entier'
chambre_type_2 = 'Chambre privée'
type1_logement = 'appartement'
type2_logement = 'maison'

if chambre_type in type_de_chambre :
    chambre_de_type = 'Logement entier '

elif chambre_type in type_de_chambre :
    chambre_de_type = 'Chambre privée '
else:
    chambre_de_type = 'Logement entier '

if type1_logement in type_de_logement:
    logement_type = 'Appartement '
elif type2_logement in type_de_logement:
    logement_type = 'Maison '
else:
    logement_type = 'Appartement '

json = {
        'Chaine': ['Airbnb'],
        'Capacité': capacite_int,
        'Chambre à coucher': chambre_int,
        'Salle de bain': salles_de_bain_int,
        'Type de logement': logement_type,
        'Type de chambre': chambre_de_type,
        'URL airbnb': url,
        'Adresse': address_trim

        }
at.insert(json)
driver.close()