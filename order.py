import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

browser = webdriver.Chrome('/Users/ziad/Downloads/order_dominos/chromedriver')

browser.get("https://www.dominos.com/en/pages/order/#!/locations/search/?type=Carryout")
browser.implicitly_wait(10)
browser.find_element_by_xpath('//*[@id="Postal_Code_Sep"]').send_keys("80301", Keys.ENTER)
#sleep and wait for page to load nearby restaurant
time.sleep(3)
button = WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="locationsResultsPage"]/div/div[2]/div[2]/div[2]/div/div[2]/div[1]/a')))
button.click()

#choose speacialty pizza and add cheeseburger pizza to cart
browser.find_element_by_xpath('//*[@id="entree-Pizza"]/a').click()
browser.find_element_by_xpath('//*[@id="categoryPage2"]/section/div/div[2]/div/a[1]').click()

#navigate to chicken and add buffalo wings
browser.find_element_by_class_name('navigation-Wings').click()
#next line ONLY for late night orders
#browser.find_element_by_xpath('//*[@id="genericOverlay"]/section/header/button').click()
time.sleep(1)
browser.find_element_by_xpath('//*[@id="categoryPage2"]/section/div/div[5]/div/a').click()
browser.find_element_by_xpath('//*[@id="pageModal"]/div/section/div/div/div/form/div/button[2]').click()

#navigate to drinks and add coke
browser.find_element_by_xpath('//*[@id="csn-AllDrinks"]/a').click()
time.sleep(1)
browser.find_element_by_xpath('//*[@id="categoryPage2"]/section/div/div[1]/div/a').click()
browser.find_element_by_xpath('//*[@id="pageModal"]/div/section/div/div/div/form/div/button[2]').click()

#navigate to sauces and get bbq
browser.find_element_by_xpath('//*[@id="csn-Sides"]/a').click()
time.sleep(1)
browser.find_element_by_xpath('//*[@id="categoryPage2"]/section/div/div[4]/div/a').click()
browser.find_element_by_xpath('//*[@id="pageModal"]/div/section/div/div/div/form/div/button[2]').click()

#checkout
time.sleep(1)
browser.find_element_by_xpath('//*[@id="js-myOrderPage"]/a').click()
browser.find_element_by_xpath('//*[@id="genericOverlay"]/section/div/div[2]/div/a').click()

#proceed to checkout
#browser.find_element_by_xpath('//*[@id="changeOrderTimingOverlay"]/div[2]/form/div/a').click()
browser.find_element_by_xpath('//*[@id="js-checkoutColumns"]/aside/div[4]/div[1]/a').click()


#enter first input field
browser.find_element_by_xpath('//*[@id="First_Name"]').send_keys("Ziad",  Keys.TAB, "AlWazzan", Keys.TAB, "q8-zayood@hotmail.com", Keys.TAB, "7864772581")
browser.find_element_by_xpath('//*[@id="EmailOptIn"]').click()

#enter car data
browser.find_element_by_xpath('//*[@id="payment-form"]/div[4]/div/div[1]/div[1]/select').send_keys("yellow", Keys.TAB, "je", Keys.TAB, "wrangler", Keys.TAB, "p")
browser.find_element_by_xpath('//*[@id="Duc_Sms_Opt_In"]').click()

#enter payment data and click check out manually















