from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time


##path to get chromedriver
url = r"C:\Users\salde\Desktop\chromedriver_win32 (1)\chromedriver.exe"

driver = webdriver.Chrome(executable_path=url)

##website to navigate to
driver.get('https://www.betfair.com/exchange/plus/')

##to accept cookies at the entry to the website
element = WebDriverWait(driver, 20).until(
    EC.element_to_be_clickable((By.XPATH, '//*[@id="onetrust-accept-btn-handler"]'))
)
element.click()

time.sleep(2)

btnCookies = driver.find_element_by_xpath('//*[@id="onetrust-accept-btn-handler"]')
btnCookies.click()

username = driver.find_element_by_xpath('//*[@id="ssc-liu"]')
username.send_keys('your_username')

time.sleep(2)

password = driver.find_element_by_xpath('//*[@id="ssc-lipw"]')
password.send_keys('your_password')
password.send_keys(Keys.ENTER)

time.sleep(2)

##clicking the horse racing tab
horseRaceBtn = driver.find_element_by_xpath('//*[@id="subnav"]/div/ul/li[5]/a')
horseRaceBtn.click()


time.sleep(2)




##race selection
race = driver.find_element_by_xpath('//*[@id="main-wrapper"]/div/div[2]/div/ui-view/ui-view/div/div/div/div/div[1]/div[2]/div/bf-todays-racing-mod/div/div/bf-todays-racing/section/div[2]/div/div[2]/div/li[6]/ul/li[1]/a/span')
race.click()


time.sleep(3)



##clicking the lay bet button
layBet = driver.find_element_by_xpath('//*[@id="main-wrapper"]/div/div[2]/div/ui-view/div/div/div[1]/div[3]/div/div[1]/div/bf-main-market/bf-main-marketview/div/div[2]/bf-marketview-runners-list[2]/div/div/div/table/tbody/tr[1]/td[5]/button/div/span[1]')
##time.time()= tempo attuale
##t_end variabile e uguale alla durata di 10 minuti
t_end = time.time() + 60 * 20



#loop through the duration of 20 min. and when odds is greater than 10, it places the bet.
while time.time() < t_end:
    input = layBet.text
    flNum = float(input)
    if int(flNum) > 10:

        layBet.click()
        ##input stake to lay

        inputStake = driver.find_element_by_xpath('//*[@id="main-wrapper"]/div/div[2]/div/ui-view/div/div/div[2]/div/div/bf-aside/div/div[1]/div/betslip/div/bf-tabs/section/div[1]/div/div/section/potentials/section/form/div/div/div/betslip-potential-bet/section/betslip-editable-bet/section/div[2]/div[2]/betslip-size-input/input')

        ##input amount stake to bet
        inputStake.send_keys('2')
        inputStake.send_keys(Keys.ENTER)
        break

