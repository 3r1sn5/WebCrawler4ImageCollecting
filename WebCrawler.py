import os
import time
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

keyword = 'full body anime character'
url = 'https://www.google.com/search?q=' + keyword + '&tbm=isch'

class crawler_images:
    def __init__(self):
        self.url = url

    def init_browser(self):
        browser = webdriver.Edge()
        browser.get(self.url)
        browser.maximize_window()
        return browser
    
    def download(self, browser, round=2):
        path = 'Downloaded_Image/{}'.format(keyword)

        if not os.path.exists(path): os.makedirs(path)

        count = 0
        pos = 0

        for i in range(round):
            img_url_dic = []
            pos += 500
            js = 'var q=document.documentElement,scrollTop=' + str(pos)
            browser.execute_script(js)
            time.sleep(3)
            img_elements = browser.find_elements(by=By.TAG_NAME, value='img')

            for img_element in img_elements:
                img_url = img_element.get_attribute('src')
                if isinstance(img_url, str):
                    if len(img_url) <= 200:
                        if 'images' in img_url:
                            if img_url not in img_url_dic:
                                try:
                                    img_url_dic.append(img_url)
                                    file_name = path + str(count) + ".jpg"
                                    r = requests.get(img_url)
                                    with open(file_name, 'wb') as f:
                                        f.write(r.content)
                                    f.close
                                    count += 1
                                    print('No. ' + str(count) + ' image is downloaded')
                                    time.sleep(0.5)
                                except:
                                    print('Failed')
    
    def run(self):
        self.__init__
        browser = self.init_browser()
        self.download(browser, 1)
        browser.close()
        print('Finish')
    
if __name__ == '__main__':
    craw = crawler_images()
    craw.run()
