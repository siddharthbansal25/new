from selenium import webdriver
from time import sleep
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
        #driver.find_element_by_xpath("//a[@href='/direct/inbox/']").click()
        sleep(1)
        s="https://www.instagram.com/"+u
        driver.get(s)
        sleep(1)
        driver.find_element_by_xpath("//a[@href='/{}/following/']".format(u)).click()
        sleep(1)
        c=0
        #while c<8:
            #driver.find_element_by_css_selector("[aria-label='Like']").click()
            #c=c+1

        driver.find_element_by_xpath("//a[@href='/populargram_insta/']").click()
        sleep(1)
        driver.find_element_by_xpath("//a[@href='/populargram_insta/following/']").click()
        sleep(2)
        count=0
        while count<10:
            driver.find_element_by_xpath("//button[@class='sqdOP  L3NKy   y3zKF     ']").click()
            count=count+1

        sleep(15)

        c=0
        while c<10:
            driver.find_element_by_xpath("//button[@class='sqdOP  L3NKy    _8A5w5    ']").click()
            driver.find_element_by_xpath("//button[@class='aOOlW -Cab_   ']").click()
            c=c+1

        sleep(5)
        driver.quit()



ob=Insta()
u=""#enter your username
p=""#enter your password
ob.login(u,p)