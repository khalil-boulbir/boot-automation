from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException  
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains
import time
import requests
import urllib.request, json 
from selenium.common.exceptions import TimeoutException, WebDriverException
def check_exists_by_xpath(xpath):
        try:
            driver.find_element_by_xpath(xpath)
        except NoSuchElementException:
            return False
        return True
emails=["yasser.mayati1@gmail.com"]
k=0 
options = webdriver.ChromeOptions()
driver = webdriver.Chrome('C:\\Users\\oussama\\Desktop\\chromedriver.exe') 
driver.set_window_size(1024,800)
driver.maximize_window()
driver.get("https://www.midasbuy.com/midasbuy/ot/redeem/pubgm")
time.sleep(3)
driver.find_element_by_xpath("//div[@class='btn login-btn']").click()
time.sleep(3)
iframe = driver.find_element_by_xpath("//iframe[@name='iframe-window']")
driver.switch_to.frame(iframe)
ActionChains(driver).double_click().perform()
ActionChains(driver).key_down(Keys.TAB).perform()
ActionChains(driver).send_keys(emails[k]).perform()
#pyautogui.hotkey('ctrl','')
time.sleep(0.5)
ActionChains(driver).key_down(Keys.TAB).perform()
ActionChains(driver).send_keys("yasser.mayati1998").perform()
time.sleep(0.5)
driver.find_element_by_xpath("//div[@class='btn sign-in-btn']").click()
time.sleep(3)
while True:
    with urllib.request.urlopen("https://testapi.sw-games.net/testWahts?fbclid=IwAR0pKTZrUvDimMG-w_eHrF-GzAbmAfQj3-EsI3TNYlvupMR2LoKhCylX7QY") as url:
        data = json.loads(url.read().decode())
    n=len(data)
    print(n)
    if len(data)!=0:
        x=0
        while x<n:
            if(len(data[x]["code"]))<5:
                driver.get("https://www.midasbuy.com/midasbuy/ot/buy/pubgm")
                time.sleep(0.5)
                driver.find_element_by_xpath("//input[@type='text']").send_keys("5731869689")#id
                time.sleep(0.5)
                p = driver.current_window_handle
                #driver.find_element_by_xpath("//p[normalize-space()='Razer Gold']").click()
                driver.execute_script("arguments[0].click();", driver.find_element(By.XPATH, "//p[normalize-space()='Razer Gold']"))
                
                driver.find_element_by_xpath(f"//li[@cr='amount_select.{30}']").click()
                time.sleep(1)
                driver.execute_script("arguments[0].click();", driver.find_element(By.XPATH, "//div[@id='buy-payBtn']"))

                #driver.find_element_by_xpath("//div[@id='buy-payBtn']").click()
                time.sleep(7)
                driver.switch_to.window(driver.window_handles[1])
                time.sleep(1)
                driver.find_element_by_xpath("//input[@id='loginEmail']").send_keys("eeeeeeeeee")
                driver.find_element_by_xpath("//input[@id='loginPassword']").send_keys("eeeeeeee")
                ActionChains(driver).send_keys(Keys.ENTER).perform()
                time.sleep(3)
                driver.execute_script("arguments[0].click();", driver.find_element(By.XPATH, "//button[@id='btn99']"))
                time.sleep(7)
                if(check_exists_by_xpath("//iframe[@title='Razer OTP']")):
                    iframe = driver.find_element_by_xpath("//iframe[@title='Razer OTP']")
                    driver.switch_to.frame(iframe)
                    time.sleep(2)
                    x=driver.find_element(By.XPATH, "//button[@class='btn arrowed']")
                    #x[9].click()
                    driver.execute_script("arguments[0].click();",x )
                    #ActionChains(driver).click(on_element=x[9]).perform()

                    time.sleep(5)
                    driver.execute_script("arguments[0].click();", driver.find_element(By.XPATH, "//button[normalize-space()='Backup Codes']"))
                    keys=open("C:\\Users\\oussama\\Desktop\\keys.txt",'r')
                    data=keys.readlines()
                    driver.find_elements_by_xpath("//input[@class=' input-otp']")[0].send_keys(data[2])
                    time.sleep(4)
                    driver.switch_to.default_content()
                if (len(driver.find_elements_by_xpath("//button[@type='button']")))==3:
                    driver.execute_script("arguments[0].click();", driver.find_elements_by_xpath("//button[@type='button']")[2])
                    time.sleep(4)
                    driver.switch_to.window(p)
                    time.sleep(3)
                    if check_exists_by_xpath("//button[@class='btn arrowed']")==True:
                        erorrs={"id":data[x]["id"],"status":'5',"note":"تمت العملية بنجاح"}
                        message=requests.post(url,json=erorrs)
                        print("succs",message.text)
                    
                else:
                    erorrs={"id":data[x]["id"],"status":'2',"note":"no money have"}
                    #message=requests.post(url,json=erorrs)
                    print("error")








