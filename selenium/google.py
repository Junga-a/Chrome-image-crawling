from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import urllib.request
import os

sname="송지효" ##검색어 입력
imagecount = 100 ##저장할 이미지 개수 지정

try:
    if not(os.path.isdir(sname)):
        os.makedirs(os.path.join(sname))
except OSError as e:
    if e.errno != errno.EEXIST:
        print("Failed to create directory!!!!!")
        raise

driver = webdriver.Chrome('C:/Users/박정아/Downloads/chromedriver_win32/chromedriver.exe')
driver.get("https://www.google.co.kr/imghp?hl=ko&tab=wi&authuser=0&ogbl")
elem = driver.find_element_by_name("q")
elem.send_keys(sname)
elem.send_keys(Keys.RETURN)

SCROLL_PAUSE_TIME = 1
# Get scroll height
last_height = driver.execute_script("return document.body.scrollHeight")
while True:
    # Scroll down to bottom
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    # Wait to load page
    time.sleep(SCROLL_PAUSE_TIME)
    # Calculate new scroll height and compare with last scroll height
    new_height = driver.execute_script("return document.body.scrollHeight")
    if new_height == last_height:
        try:
            driver.find_element_by_css_selector(".mye4qd").click()
        except:
            break
    last_height = new_height

images = driver.find_elements_by_css_selector(".rg_i.Q4LuWd")
imagecount = imagecount+1
count = 1

for image in images:
    try:
        image.click()
        time.sleep(2)
        imgUrl = driver.find_element_by_xpath('/html/body/div[2]/c-wiz/div[3]/div[2]/div[3]/div/div/div[3]/div[2]/c-wiz/div[1]/div[1]/div/div[2]/a/img').get_attribute("src")
        opener=urllib.request.build_opener()
        opener.addheaders=[('User-Agent','Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1941.0 Safari/537.36')]
        urllib.request.install_opener(opener)
        urllib.request.urlretrieve(imgUrl, str(count) + ".jpg")
        count = count + 1
        if(count==imagecount):
            break
    except:
        pass

for i in range(1 ,imagecount):
    os.rename("C:/Users/박정아/Desktop/크롬 이미지 크롤링/"+str(i)+".jpg", "C:/Users/박정아/Desktop/크롬 이미지 크롤링/" +sname+ "/" + str(i) + ".jpg")

driver.close()