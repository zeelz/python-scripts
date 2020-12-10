from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
CHROMEDRIVER = '/Users/kemekenneth/chromedriver'
def voter():
    driver = webdriver.Chrome(CHROMEDRIVER)
    driver.get('https://vendorsaward.womeninportharcourt.com/')
    time.sleep(5)
    for i in range(10):
        mamapot = driver.find_element_by_id('answer[18]').click()
        time.sleep(1)
        vote = driver.find_element_by_xpath('/html/body/div/div/div/section[14]/div/div/div[1]/div/div/div/div/div/div/div/div/div/div/form/div[2]/a')
        vote.send_keys(Keys.RETURN)
        time.sleep(3)
        driver.refresh()
    driver.close()
if __name__ == '__main__':
    voter()