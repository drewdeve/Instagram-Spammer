from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.proxy import Proxy, ProxyType
from time import sleep
import csv

num_users = int(input('Enter the number how many users will be added to the group: '))

proxy = Proxy()
proxy.proxy_type = ProxyType.MANUAL
proxy.http_proxy = '201.234.53.214:999'

capabilities = webdriver.DesiredCapabilities.CHROME
proxy.add_to_capabilities(capabilities)

driver = webdriver.Chrome(ChromeDriverManager().install(), desired_capabilities=capabilities)

username = input('Enter your username: ')
password = input('Enter your password: ')

file = 'instagramspammer/forex_russia_nk_430_followers.csv'

message = """ MSG """

users = []

class InstaSpammer:
    def __init__(self, username, password, file, users, message):
        self.username = username
        self.password = password
        self.file = file
        self.users = users
        self.message = message
        self.base_url = 'https://www.instagram.com/'
        self.bot = driver
        self.open_file()
        self.login()

    def open_file(self):
        with open(file) as f:
            rows = csv.reader(f,delimiter=",",lineterminator="\n")
            next(rows, None)
            for row in rows:
                user = {}
                user['username'] = row[1]
                users.append(user)

    def login(self):
        self.bot.get(self.base_url)
        try:
            self.bot.find_element_by_xpath('/html/body/div[4]/div/div/button[1]').click()
        except:
            pass
        enter_username = WebDriverWait(self.bot, 20).until(
            expected_conditions.presence_of_element_located((By.NAME, 'username')))
        enter_username.send_keys(self.username)
        enter_password = WebDriverWait(self.bot, 20).until(
            expected_conditions.presence_of_element_located((By.NAME, 'password')))
        enter_password.send_keys(self.password)
        enter_password.send_keys(Keys.RETURN)
        sleep(5)

        #first popup box
        self.bot.find_element_by_xpath('/html/body/div[1]/section/main/div/div/div/div/button').click()
        sleep(3)

        #second popup box
        self.bot.find_element_by_xpath('/html/body/div[6]/div/div/div/div[3]/button[2]').click()
        sleep(4)

        #direct button
        self.bot.find_element_by_xpath('/html/body/div[1]/section/nav/div[2]/div/div/div[3]/div/div[2]/a').click()
        sleep(3)

        for i in range(6):
            x = 0
            input_users = []
            print("Sending messages started:", i)
            for user in users[:]:
                x += 1
                input_users.append(user)
                users.remove(user)
                if x >= num_users:
                    break

            #click on pencil icon
            self.bot.find_element_by_xpath('/html/body/div[1]/section/div/div[2]/div/div/div[1]/div[1]/div/div[3]/button').click()
            sleep(2)

            for user in input_users:
                if user['username'] == "":
                    continue
                #enter the username
                self.bot.find_element_by_xpath('/html/body/div[6]/div/div/div[2]/div[1]/div/div[2]/input').send_keys(user['username'])
                sleep(10)
                #click on the username
                self.bot.find_element_by_xpath('/html/body/div[6]/div/div/div[2]/div[2]/div').click()
                sleep(10)
            
            #next button
            self.bot.find_element_by_xpath('/html/body/div[6]/div/div/div[1]/div/div[2]/div/button').click()
            sleep(4)

            #click on message area
            send = self.bot.find_element_by_tag_name('textarea')

            #types message
            send.send_keys(self.message)
            sleep(1)

            #send message
            send.send_keys(Keys.RETURN)
            sleep(2)

def init():
    InstaSpammer(username, password, file, users, message)

    #when our program ends it will show "done".
    print("DONE")

init()
