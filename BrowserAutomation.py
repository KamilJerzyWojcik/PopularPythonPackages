from selenium import webdriver
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_argument("start-maximized")

browser = webdriver.Chrome(f"C:\chromedriver", options=chrome_options)

browser.get("https://github.com")

signin_link = browser.find_element_by_link_text("Sign in")
signin_link.click()
username_box = browser.find_element_by_id("login_field")
username_box.send_keys("kamil.jerzy.wojcik@gmail.com")

password_box = browser.find_element_by_id("password")
password_box.send_keys("hMH-ETG-e7D-t2H")
password_box.submit()
assert "KamilJerzyWojcik" in browser.page_source

profile_link = browser.find_element_by_class_name("user-profile-link")
link_label = profile_link.get_attribute("innerHTML")
assert "KamilJerzyWojcik" in link_label

browser.quit()