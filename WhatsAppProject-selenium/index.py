from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

message_for_who = str(input("The message for who ?"))
whats_the_message = str(input("What's the message ? "))
hm_times = int(input("How many times you wanna send it?"))


class Whatsapp():
    def __init__(self):
        self.driverProfile = webdriver.ChromeOptions()
        self.driverProfile.add_experimental_option('prefs', {'intl.accept_languages': 'en,en_US'})
        self.driver = webdriver.Chrome('chromedriver.exe', options=self.driverProfile)

    def signIn(self):
        url = "https://web.whatsapp.com/"
        self.driver.get(url)
        self.driver.maximize_window()
        time.sleep(7)

        find_theuser = self.driver.find_element_by_xpath("//*[@id='side']/div[1]/div/label/div/div[2]")
        find_theuser.send_keys(message_for_who.strip())

        time.sleep(2)
        click_find_theuser = self.driver.find_element_by_class_name('_3CneP').click()
        time.sleep(2)

        text = self.driver.find_element_by_xpath("//*[@id='main']/footer/div[1]/div[2]/div")
        i = 0
        while i < hm_times:
            i += 1
            text.send_keys(whats_the_message.strip())
            text.send_keys(Keys.ENTER)


    def signOut(self):
        time.sleep(3)
        find_the_logout = self.driver.find_element_by_xpath("//*[@id='side']/header/div[2]/div/span/div[3]/div").click()
        log_out = self.driver.find_element_by_xpath("//*[@id='side']/header/div[2]/div/span/div[3]/span/div/ul/li[7]/div").click()
        self.driver.close()


lets_start = Whatsapp()
lets_start.signIn()
lets_start.signOut()