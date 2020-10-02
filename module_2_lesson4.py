import time
import math
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    link='http://suninjuly.github.io/explicit_wait2.html'
    browser=webdriver.Chrome()
    browser.get(link)
    
    result_1=WebDriverWait(browser,12).until (EC.text_to_be_present_in_element((By.ID, "price"), "100"))
        
    button_1 = browser.find_element_by_id("book")
    button_1.click()
    
    numb_1=browser.find_element_by_id('input_value')
    x=numb_1.text
    result_2=calc(x)
    
    ans=browser.find_element_by_id('answer')
    ans.send_keys(result_2)
    
    button_2 = browser.find_element_by_id("solve")
    button_2.click()
    


finally:
    time.sleep(5)
    browser.quit()