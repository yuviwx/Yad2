import bs4
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import time


browser = webdriver.Chrome()
browser.implicitly_wait(10)
browser.set_window_size(1024, 600)
browser.maximize_window()

browser.get('https://www.yad2.co.il/')
wait = WebDriverWait(browser, 10)
element = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,
                                                 '#file-list > div > div.menu > div:nth-child(3) > div > div > '
                                                 'div.searches_elements > div:nth-child(4)')))
elemGip = browser.find_element_by_css_selector(
    '#file-list > div > div.menu > div:nth-child(3) > div > div > div.searches_elements > div:nth-child(4)')
elemGip.click()

element1 = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,
                                                  '#__layout > div > main > div > div.main_body > '
                                                  'div.LD_search_wrapper > div > form > ul > li:nth-child(1) > div > '
                                                  'div > div:nth-child(1) > div > label > span.input-container.pt-5 > '
                                                  'input')))
elemSog = browser.find_element_by_css_selector(
    '#__layout > div > main > div > div.main_body > div.LD_search_wrapper > div > form > ul > li:nth-child(1) > div > '
    'div > div:nth-child(1) > div > label > span.input-container.pt-5 > input')
elemSog.click()
elemSog.send_keys('סוזוקי')
elemSog.send_keys(Keys.ARROW_DOWN)


element2 = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,
                                                      '#__layout > div > main > div > div.main_body > '
                                                      'div.LD_search_wrapper > div > form > ul > li:nth-child(1) > '
                                                      'div > div > div.dropdown_content > div > ul > li:nth-child(40) '
                                                      '> label > span.checkmark')))
elemSuzuki = browser.find_element_by_css_selector(
    '#__layout > div > main > div > div.main_body > div.LD_search_wrapper > div > form > ul > li:nth-child(1) > div > '
    'div > div.dropdown_content > div > ul > li:nth-child(40) > label > span.checkmark')
elemSuzuki.click()

elementX = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,
                                                      '#__layout > div > main > div > div.main_body > '
                                                      'div.LD_search_wrapper > div > form > div > div > div > '
                                                      'button.tooltip_button')))
elemX = browser.find_element_by_css_selector(
    '#__layout > div > main > div > div.main_body > div.LD_search_wrapper > div > form > div > div > div > '
    'button.tooltip_button')
elemX.click()

element3 = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,
                                                  '#__layout > div > main > div > div.main_body > '
                                                  'div.LD_search_wrapper > div > form > ul > li:nth-child(2) > div > '
                                                  'div > div:nth-child(1) > div > label > span.input-container.pt-5 > '
                                                  'input')))
elemSog2 = browser.find_element_by_css_selector(
    '#__layout > div > main > div > div.main_body > div.LD_search_wrapper > div > form > ul > li:nth-child(2) > div > '
    'div > div:nth-child(1) > div > label > span.input-container.pt-5 > input')
elemSog2.click()
elemSog2.send_keys(r"ג'ימני")
elemSog2.send_keys(Keys.ARROW_DOWN)



# element4 = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,
#                                                  '#__layout > div > main > div > div.main_body > '
#                                                  'div.LD_search_wrapper > div > form > ul > li:nth-child(2) > div > '
#                                                  'div > div.dropdown_content > div > ul > '
#                                                  'li.option_item.multi_option_item.hovered_option > label > '
#                                                  'span.checkmark')))
# browser.implicitly_wait(10)
elemJimini = browser.find_element_by_css_selector(
    '#__layout > div > main > div > div.main_body > div.LD_search_wrapper > div > form > ul > li:nth-child(2) > div > '
    'div > div.dropdown_content > div > ul > li.option_item.multi_option_item.hovered_option > label > span.checkmark')
elemJimini.click()

element5 = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,
                                                  '#__layout > div > main > div > div.main_body > '
                                                  'div.LD_search_wrapper > div > form > ul > li.search_column.col_x2 '
                                                  '> button')))
elemSearch = browser.find_element_by_css_selector(
    '#__layout > div > main > div > div.main_body > div.LD_search_wrapper > div > form > ul > li.search_column.col_x2 '
    '> button')
elemSearch.click()

browser.implicitly_wait(10)
url = browser.current_url

res = requests.get(url)
soup = bs4.BeautifulSoup(res.text, 'html.parser')
div = soup.findAll('div', class_="price")
lst = []
count = 0

for price in div:
    price1 = price.text.strip()
    price1 = price1[:-1].replace(',', '')
    try:
        lst.append(int(price1))
    except ValueError:
        count += 1
        continue
lst.sort()
print(lst)
print("ב6 הצעות לא צוין מחיר".format(count))

browser.quit()
