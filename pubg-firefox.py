from xml.dom.minidom import Element
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
from selenium.webdriver.chrome import options
options = webdriver.ChromeOptions()
options.add_argument("--headless") # Runs Chrome in headless mode.
options.add_argument('--no-sandbox') # Bypass OS security model
options.add_argument('--disable-gpu')
def check_exists_by_xpath(xpath):
        try:
            driver.find_element_by_xpath(xpath)
        except NoSuchElementException:
            return False
        return True
emails=["ééééé"
        
        ]
k=0 
while True:
    time.sleep(7)
    with urllib.request.urlopen("https://sw-games.net/api/ca/23") as url:
        data = json.loads(url.read().decode())
    n=len(data)
    print(n)
    x=n
    h=0
    cpt=0
    try:
        if(len(data))>2 :
            if len(data[h]["code"])>5:
                #driver=webdriver.Chrome("/home/khalil/Documents/scrpits/chromedriver")
                driver = webdriver.Firefox(executable_path='C:\\Users\\ELZERO\\Desktop\\boots\\geeckodriver.exe')
                #driver = webdriver.Chrome()
                driver.set_window_size(1024,800)
                driver.maximize_window()
        
                driver.get("https://www.midasbuy.com/midasbuy/ot/redeem/pubgm")
                time.sleep(0.5)
                if(check_exists_by_xpath("//div[@class='btn login-btn']")==True):
                    driver.find_element_by_xpath("//div[@class='btn login-btn']").click()
                    time.sleep(1.5)
                    iframe = driver.find_element_by_xpath("//iframe[@name='iframe-window']")
                    driver.switch_to.frame(iframe)
                    if k<len(emails):
                        driver.find_element_by_xpath("//input[@type='text']").send_keys(emails[k])
                        driver.find_element_by_xpath("//input[@type='password']").send_keys('ééééééééé')
                        time.sleep(0.5)
                        driver.find_element_by_xpath("//div[@class='btn sign-in-btn']").click()
                        time.sleep(0.5)
                        k=k+1
                    else:
                        k=0
                else:
                    url="https://sw-games.net/api/update"
                    erorrs={"id":data[x]["id"],"status":'4',"note":"هناك خطا في عملية السكراب"}
                    message=requests.post(url,json=erorrs)
                    print("errors 4",message.text)
                login=len(data[x]["code"])
              
                while (x=>1) and (data[x]["id_game"]=="23") and (login > 7):
                    time.sleep(0.5)
                    
                    time.sleep(3)
                    print(data[x]["game_id"])
                    e=driver.find_elements_by_xpath("//input[@class='input']")
                    e[0].send_keys(data[x]["game_id"])#id
                    driver.find_element_by_xpath("//div[@class='btn']").click()
                    time.sleep(3)
                    driver.get_screenshot_as_file('')
                    if( check_exists_by_xpath("//p[@class='error-tips show']")==True):
                        if "Invalid Game " in driver.find_element_by_xpath("//p[@class='error-tips show']").text:
                            print("put true id_player")
                            url="https://sw-games.net/api/update"
                            erorrs={"id":data[x]["id"],"status":'3',"note":"الايدي غلط"}
                            message=requests.post(url,json=erorrs)
                            print("errors 3",message.text)
                            x=x-1
                            
                    else:
                        e[1].send_keys(data[x]["code"])#code
                        time.sleep(1)
                        driver.find_element_by_xpath("//div[@class='btn-box']").click()
                        time.sleep(5)
                        if  ("Invalid code, please try again." in  driver.find_elements_by_xpath("//p[@class='error-tips']")[1].text) :
                                print("hello2")
                                url="https://sw-games.net/api/update"
                                erorrs={"id":data[x]["id"],"status":'2',"note":"كود الخصم خاطئ"}
                                message=requests.post(url,json=erorrs)
                                print("errors 2",message.text)
                                
                                x=x-1
                        else:
                            elment=driver.find_elements_by_xpath("//span[@class='blue-color']")
                            if 'Turkey' in elment[len(elment)-1].text:
                                url="https://sw-games.net/api/update"
                                erorrs={"id":data[x]["id"],"status":'3',"note":"البلد تركيا"}
                                message=requests.post(url,json=erorrs)
                                print("errors 2",message.text)
                                x=x-1
                            else:
                                driver.find_element_by_xpath("//div[@class='btn btn-submit']").click()               
                            
                                time.sleep(2)
                                if(check_exists_by_xpath("//p[@class='x-title']")==True):
                                    elment=driver.find_element_by_xpath("//p[@class='x-title']")
                                    
                                    if "Send to this account" in driver.page_source:
                                        print("You have already redeemed")
                                        url="https://sw-games.net/api/update"
                                        erorrs={"id":data[x]["id"],"status":'3',"note":"الكود مستعمل سابقا"}
                                        message=requests.post(url,json=erorrs)
                                        print("errors 3",message.text)
                                        x=x-1
                                    
                                    else:
                                        break
                                    
                                elif(check_exists_by_xpath("//div[@class='title']")==True):
                                    elment=driver.find_element_by_xpath("//div[@class='title']")
                                    if "Your redeem was successful." in elment.text  :
                                        print("Your redeem was successful.")
                                        url="https://sw-games.net/api/update"
                                        erorrs={"id":data[x]["id"],"status":'5',"note":"تمت العملية بنجاح"}
                                        message=requests.post(url,json=erorrs)
                                        print("status",message.text)
                                        
                                        x=x-1
                                    else:
                                        break
                                    
                                else:
                                    print("false")
                    x=x-1
                    driver.get("https://www.midasbuy.com/midasbuy/ot/redeem/pubgm")
                    h=h+1
            else:
                    url="https://sw-games.net/api/update"
                    erorrs={"id":data[h]["id"],"status":'4',"note":"  ريزر "}
                    message=requests.post(url,json=erorrs)
                    print("status",message.text)
                    h=h+1
                   
        
    except WebDriverException:
        erorrs={"id":data[x]["id"],"status":'4',"note":"هناك خطا في عملية السكراب"}
        message=requests.post(url,json=erorrs)
        print("status",message.text)
        x=x-1
        driver.close()
    

