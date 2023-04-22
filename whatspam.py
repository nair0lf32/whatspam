from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
import time

options = Options()
options.add_argument("disable-gpu")
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option('useAutomationExtension', False)

driver = webdriver.Chrome(ChromeDriverManager().install(), chrome_options=options)
driver.implicitly_wait(120)
driver.get('https://web.whatsapp.com/')

#  ************************ CONFIGURATION REQUIRED ************************    #########
########################################################################################
name = "+229 67 24 23 36"
msg = " Here goes the spam!"
count = 4   # the spam rate, number of messages (don't be a maniac)
gap = float(1.0)   # spam rate, time between messages (don't be a savage)
########################################################################################

user = driver.find_element_by_xpath('//span[@title = "{}"]'.format(name))
user.click()

msg_box = driver.find_element_by_xpath('//div[@data-tab = "9"]')    # selector 1

for i in range(count):
    msg_final = '<Status: ' + str(i+1) + '/' + str(count) + '>' + msg
    start_time = time.time()
    msg_box.send_keys(msg_final)
    button = driver.find_element_by_class_name('_4sWnG')      # selector 2
    button.click()
    if gap > 0:
        time.sleep(gap)


msg_final = "{0} messages envoyés en {1} secondes".format(count, (round((time.time() - start_time), 2)))
msg_box.send_keys(msg_final)
button = driver.find_element_by_class_name('_4sWnG')       # selector 3
button.click()

time.sleep(30)
driver.close()
