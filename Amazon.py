from selenium import webdriver
from time import sleep
from bs4 import BeautifulSoup
import requests
import smtplib

headers = {"User-Agent": 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36'}
site = input("Please provide URL of item on Amazon SG: ")
email = 
password = 
send_to = 

def check_price():

	browser = requests.get(site,headers=headers)
	sleep(2)

	soup = BeautifulSoup(browser.content,'html.parser')

	prices = []

	title = soup.find(id="productTitle").get_text().strip()
	price = float(soup.find(id="priceblock_ourprice").get_text().replace("S$",""))
	delivery = soup.find(class_="a-color-base a-text-bold").get_text().strip()
	if "FREE" in delivery:
		delivery = float(0)
	else:
		float(delivery)
	total_price = float(price+delivery)

	prices.append(total_price)

	if(total_price<prices[0]):
		send_mail()

	print(title)
	print(price)
	print(delivery)
	print(prices)

def send_mail():
	server = smtplib.SMTP('smtp.gmail.com',587)
	server.ehlo()
	server.starttls()
	server.ehlo()
	
	server.login(email,password)

	subject = "Price dropped!"
	body = "Check out the Amazon link:" + site

	msg = f"Subject: {subject}\n\n{body}"

	server.sendmail(email,send_to,msg)

	print("Email sent")

	server.quit()

while (True):
	check_price()
	sleep(86400)

		
check_price()
