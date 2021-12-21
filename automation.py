from selenium import webdriver

chrome_browser = webdriver.Chrome('./chromedriver')
# print(chrome_browser)
chrome_browser.maximize_window()

chrome_browser.get('https://www.seleniumeasy.com/python')

# print('TestNG Tutorials | Selenium Easy' in chrome_browser.title)

# assert 'TestNG Tutorials | Selenium Easy' in chrome_browser.title

# assert 'Show Message' in chrome_browser.page_source # It will shows an error

user_message = chrome_browser.find_element_by_id("edit-search-block-form--2") # it will find this id

user_message.clear()
user_message.send_keys('How extra cool i am!') # It will set this message on search box

search = chrome_browser.find_element_by_class_name('input-group-btn')
search.click()

chrome_browser.close() # It will close the browser
chrome_browser.quit() # It will quit the whole browser






