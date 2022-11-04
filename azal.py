from xml.dom.minidom import Element
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException  
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains
import time
import re
from selenium.common.exceptions import TimeoutException, WebDriverException
import requests 
def check_exists_by_xpath(xpath):
        try:
            driver.find_element_by_xpath(xpath)
        except NoSuchElementException:
            return False
        return True

names=[]
driver = webdriver.Firefox(executable_path='C:\\Users\\oussama\\Desktop\\geckodriver.exe')
driver.get("https://www.jawaker.com/ar/users/sign_in")
time.sleep(0.5)
driver.find_element(By.XPATH, "//input[@id='user_email']").send_keys("éééé")
driver.find_element(By.XPATH, "//input[@id='user_password']").send_keys("ééééé")
time.sleep(2)
ActionChains(driver).send_keys(Keys.ENTER).perform()
time.sleep(3.5)
driver.find_element(By.XPATH, "//span[contains(text(),'الأندية')]").click()
time.sleep(2)
id="y_a_h_i_y"
driver.find_element(By.XPATH, "//input[@placeholder='ابحث عن أصدقاء...']").send_keys(id)
time.sleep(5)
elements=driver.find_elements(By.XPATH, "//li[@class=' ']")
for i in elements:
    names.append(i.text)
for j in range(len(names)):
    if id in names[j]:
        cpt=j
        print(j)
time.sleep(2)
element=driver.find_elements(By.XPATH, "//li[@class=' ']")[cpt]
driver.execute_script("arguments[0].click();", element)
time.sleep(4)
element=driver.find_element(By.XPATH, "//a[contains(text(),'أرسل توكنز')]")
driver.execute_script("arguments[0].click();", element)
time.sleep(1)
driver.find_element(By.XPATH, "//input[@id='amount_of_tokens']").send_keys(Keys.CONTROL,'a')
time.sleep(1)
driver.find_element(By.XPATH, "//input[@id='amount_of_tokens']").send_keys(Keys.DELETE)
time.sleep(0.5)
driver.find_element(By.XPATH, "//input[@id='amount_of_tokens']").send_keys("11")
driver.find_element(By.XPATH, "//a[@class='btn btn-small btn-primary']").click()
time.sleep(0.5)
driver.find_element(By.XPATH, "//input[@value='هل أنت متأكد؟']").click()
driver.save_screenshot(f"C:\\Users\\oussama\\Desktop\\{id}.png")
driver.close()
driver.quit()








