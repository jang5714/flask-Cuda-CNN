from bs4 import BeautifulSoup
from selenium import webdriver
import time
path = 'C:\\Users\\bitcamp\\___\\flaskproject\\data\\chromedriver.exe'
class VisitKorea(object):
    def __init__(self):
        query_txt = input('Input Keyword')
        driver = webdriver.Chrome(path)
        driver.get('https://nid.naver.com/nidlogin.login')
        driver.implicitly_wait(3)

        driver.find_element_by_id('id_line').send_keys('lionx3')
        driver.find_element_by_id('pw').send_keys('Wkd1598!@')
        driver.find_element_by_class_name('btn_login').click()
        driver.implicitly_wait(3)
        # driver.find_element_by_link_text('검색').click()


if __name__ == '__main__':
    VisitKorea()