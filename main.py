from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import os
from dotenv import load_dotenv
import requests


load_dotenv()


URL_ZILLOW=os.getenv("ZILLOW")
response=requests.get(URL_ZILLOW).text


soup=BeautifulSoup(response,"html.parser")


address_list=soup.find_all(name="address")
price_list=soup.find_all(name="span",class_="PropertyCardWrapper__StyledPriceLine")
link_list=soup.find_all(name="a",class_="property-card-link")


URL_GOOGLE_DOCS=os.getenv("GOOGLE_DOCS")


chrome_options=webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach",True)


# for i in range(len(link_list)):
#     print(link_list[i].get_attribute_list("href"))

driver=webdriver.Chrome(options=chrome_options)



for i in range(len(address_list)):
    driver.get(URL_GOOGLE_DOCS)
    
    
    add_field=driver.find_element(by=By.XPATH,value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
    add_field.send_keys(address_list[i].getText())


    price_field=driver.find_element(by=By.XPATH,value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
    price_field.send_keys(price_list[i].getText())


    link_field=driver.find_element(by=By.XPATH,value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')
    link_field.send_keys(link_list[i].get_attribute_list("href"))


    submit=driver.find_element(by=By.XPATH,value='//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div/span/span')
    submit.click()

driver.quit()