#!/usr/bin/env python

from selenium import webdriver
import time

#Simple python file leveraging the work the folks at http://www.stachliu.com have done collating around 100 sharepoint urls to check that permissioning is correct.
#The file below comes from http://www.stachliu.com/resources/tools/sharepoint-hacking-diggity-project/

file = open('SharePoint-UrlExtensions-18Mar2012.txt','r')
base = 'https://sharepoint.mydomain.com'
username = 'administrator'
password = 'password'
count = 0
chrome = webdriver.Chrome()

#Login and create the session
login = base + '/_layouts/FBA/Login.aspx'
chrome.get(login)
chrome.find_element_by_id("ctl00_PlaceHolderMain_signInControl_username").send_keys(username)
chrome.find_element_by_id("ctl00_PlaceHolderMain_signInControl_password").send_keys(password)
chrome.find_element_by_id("ctl00_PlaceHolderMain_signInControl_loginbutton").click()

#Try all URLs and take screenshots
for line in file:
   time.sleep(2)
   count = count + 1
   url = base + line
   #name = url.replace('/','-')
   name = 'images/%s.jpg' % url.replace('/','-') 
   print "Trying..... " + url
   chrome.get(url)
   print "Saving..... " + name
   chrome.save_screenshot(name)

print count
