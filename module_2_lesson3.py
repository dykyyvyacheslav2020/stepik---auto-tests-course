import time
from selenium import webdriver
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    link='http://suninjuly.github.io/redirect_accept.html'
    browser=webdriver.Chrome()
    browser.get(link)
    button_1=browser.find_element_by_tag_name('button')
    button_1.click()
    
    new_wind=browser.window_handles[1]
    sel=browser.switch_to.window(new_wind)
    
      
    numb_1=browser.find_element_by_id('input_value')
    x=numb_1.text
    result=calc(x)
    
    ans=browser.find_element_by_id('answer')
    ans.send_keys(result)
    
    button_2=browser.find_element_by_tag_name('button')
    button_2.click()
    
finally:
    time.sleep(10)
    browser.quit()
    