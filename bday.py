from selenium import webdriver
from time import sleep,localtime
driver=webdriver.Chrome(executable_path="D:\chromedriver")
driver.get("https://www.instagram.com/")
sleep(2)
class Insta:
    def  login(self,username,password):
        driver.find_element_by_name("username").send_keys(username)
        driver.find_element_by_name("password").send_keys(password)
        driver.find_element_by_xpath("//button[@type='submit']").click()
        sleep(4)
        driver.find_element_by_xpath("//button[contains(text(),'Not Now')]").click()
        sleep(1)
        driver.find_element_by_xpath("//button[contains(text(),'Not Now')]").click()
        sleep(1)
        c = localtime().tm_mon
        d = localtime().tm_mday
        if c==9 and d==2:
            driver.find_element_by_css_selector("[aria-label='Direct']").click()
            sleep(5)
            driver.find_element_by_xpath("//button[contains(text(),'Send Message')]").click()
            sleep(3)
            driver.find_element_by_xpath("//input[@placeholder='Search...']").send_keys("siddharthbansal")
            sleep(5)
            driver.find_element_by_xpath("//button[@class='dCJp8 ']").click()
            sleep(1)
            driver.find_element_by_xpath("//button[@class='sqdOP yWX7d    y3zKF   cB_4K  ']").click()
            sleep(2)
            driver.find_element_by_xpath("//textarea[@placeholder='Message...']")\
                .send_keys("happy birthday")




ob=Insta()
u=""#enter your username
p=""#enter your password

ob.login(u,p)