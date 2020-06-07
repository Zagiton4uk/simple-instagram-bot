from selenium import webdriver
import os
import time


import configparser

# a class is a template
class InstagramBot:
    
    def __init__(self, username, password): 
        """
        
        notes: 
        username: fill in accordingly
        password: fill in accordingly
        
        
        """
    
    
        self.username = username
        self.password = password
        self.base_url= 'https://www.instagram.com'
        # pass a script for chrome to boot up and launch the website
        self.driver = webdriver.Chrome('./chromedriver.exe')
        
        self.login()
        
        
        
        
    def login(self):
        self.driver.get('{}/accounts/login/'.format(self.base_url))
        
        # pass username onto username textbox using div name
        self.driver.find_element_by_name('username').send_keys(self.username)
        # pass passward onto password textbox using div name
        self.driver.find_element_by_name('password').send_keys(self.password)
      
        # locates login button by identifying xpath
        self.driver.find_elements_by_xpath("//div[contains(text(), 'Log In')]")[0].click()
        
        time.sleep(2)
        
    def nav_user(self, user):
        self.driver.get('{}/{}'.format(self.base_url, user))
        
    def follow_user(self,user):
        self.nav_user(user)
        follow_button = self.driver.find_elements_by_xpath("//button[contains(text(), 'Follow')]")[0]
        follow_button.click()

if __name__ == '__main__':
    
     
    config_file_path = './config.ini'
    cparser = configparser.ConfigParser()
    
    cparser.read(config_file_path)
    username = cparser['IG_AUTH']['USERNAME']
    password = cparser['IG_AUTH']['PASSWORD']
    ig_bot = InstagramBot(username, password)
    
    
    #ig_bot.nav_user('ufc')
    ig_bot.follow_user('ufc')
    
    
    
    
    print(ig_bot.username)