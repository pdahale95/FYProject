from selenium import webdriver
from user import User
from bs4 import BeautifulSoup

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

import requests

f = open('users_ids.txt', 'a')

def fetch_user_list(start, driver):
	
	baseUrl = "https://discuss.codechef.com/users/?sort=karma&page="
	userLink = baseUrl + str(start)

	driver.get(userLink)
	print('reach user list page '+ userLink)

	
	try:
		userList = driver.find_element_by_class_name('userList')
		lis = userList.find_elements_by_class_name('thumb')
		for li in lis: 
			a = li.find_element_by_tag_name('a')
			aas = a.get_attribute('href').split('/')
			# print aas[5]
			f.write(aas[5] + '\n')
			
	
	except Exception as e:
		print('element not found')
		print(e)
		prob = None
	else:
		pass
	finally:
		pass
	
	
	if start < 4763:
		fetch_user_list(start+1, driver)
		
	

driver = webdriver.Chrome('C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe')
# fetch_user('anudeep2011', driver)
# fetch_user('sherlock_holms', driver)
fetch_user_list(101, driver)
# fetch_user('paragpachpute', driver)
# fetch_user('pranay0007', driver)
driver.close()