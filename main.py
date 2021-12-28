from time import sleep
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys

chrome_driver_path = "C:/Users/buski/Documents/Development/chromedriver.exe"

# ------- Details --------------------
My_Mail = "Insert your username/mail"
My_pass = "Insert your password"
similar_account = "Insert similar Instagram account"
# ------------------------------------

instagram_url = "https://www.instagram.com/"
login_url = "accounts/login/"



class InstaFollowers:
    def __init__(self):
        self.driver = webdriver.Chrome(executable_path=chrome_driver_path)

    def login(self):
        self.driver.get(url=instagram_url + login_url)
        sleep(2)

        username = self.driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[1]/div/label/input')
        username.send_keys(My_Mail)

        password = self.driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[2]/div/label/input')
        password.send_keys(My_pass)

        password.send_keys(Keys.ENTER)
        sleep(5)

    def find_followers_and_follow(self):
        self.driver.get(url=instagram_url + similar_account)
        sleep(5)
        his_followers = self.driver.find_element_by_xpath(
            '//*[@id="react-root"]/section/main/div/header/section/ul/li[2]/a')
        his_followers.click()
        sleep(5)

        for i in range(1, 1001):
            try:
                followers = self.driver.find_element_by_xpath(
                    f'/html/body/div[6]/div/div/div[2]/ul/div/li[{i}]/div/div[2]/button')
            except NoSuchElementException:
                followers = self.driver.find_element_by_xpath(
                    f'/html/body/div[6]/div/div/div[2]/ul/div/li[{i}]/div/div[3]/button')
            followers.click()
            sleep(1)
            self.driver.execute_script("window.scrollTo(0, 10)")

        self.driver.quit()


bot = InstaFollowers()
bot.login()
bot.find_followers_and_follow()

