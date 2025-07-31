from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager



if __name__ == '__main__':

    file = open('./input.txt').read()

    print('====Removing Punctuations====')
    for i in './,?-()|:;':
        file.replace(i, '')
    print('====Punctuation removed====')


    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    # driver.maximize_window()
    driver.get('https://translate.google.com/?sl=hi&tl=en&op=translate')
    time.sleep(2)

    # turn off the google input tool
    input_tool = driver.find_element(By.XPATH, '//*[@id="itamenu"]/span/div/a[1]/span')
    input_tool.click()

    # find textarea
    textarea = driver.find_element(By.XPATH, '//*[@id="yDmH0d"]/c-wiz/div/div[2]/c-wiz/div[2]/c-wiz/div[1]/div[2]/div[3]/c-wiz[1]/span/span/div/textarea')
    
    for word in file.split():
        textarea.clear()
        textarea.send_keys(word)
        
        time.sleep(1)

        try:
            lang = driver.find_element(By.XPATH, '//*[@id="yDmH0d"]/c-wiz/div/div[2]/c-wiz/div[2]/c-wiz/div[1]/div[2]/div[3]/c-wiz[1]/div[3]/div/div/div')
            if(lang):
                print(word, 'English')
        except:
            # try:
            output = driver.find_element(By.XPATH, '//*[@id="yDmH0d"]/c-wiz/div/div[2]/c-wiz/div[2]/c-wiz/div[1]/div[2]/div[3]/c-wiz[1]/div[2]/div[1]')
            # print(word, output.text)
            with open('output.txt', "a", encoding="utf-8") as f:
                f.write(word+' '+ str(output.text)+'\n')
            # except:
            #     print(f'{word} could not be converted')


    time.sleep(5)