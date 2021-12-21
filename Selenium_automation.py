from selenium import webdriver
chrome_browser = webdriver.Chrome('./chromedriver')
chrome_browser.get('https://www.tutorialspoint.com/market/login.jsp?v=1.3')
chrome_browser.maximize_window()

email = chrome_browser.find_element_by_id("user_email")
email.clear()
email.send_keys("stranger@gmail.com")

password = chrome_browser.find_element_by_id("user_password")
password.clear()
password.send_keys("1234567836")

login = chrome_browser.find_element_by_id("user_login")
login.click()

