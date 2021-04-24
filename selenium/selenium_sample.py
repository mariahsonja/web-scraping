from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager

username = "<your-email>"
password = "<your-password>"

# driver = webdriver.Chrome(ChromeDriverManager().install())
# driver = webdriver.Chrome("/Users/msonjap/.wdm/drivers/chromedriver/mac64/89.0.4389.23/chromedriver")
driver = webdriver.Chrome()
driver.get("https://twitter.com/login")


user_login = driver.find_element_by_id("email")
user_login.send_keys(username)
user_login = driver.find_element_by_id("pass")
user_login.send_keys(password)

user_login.send_keys(Keys.RETURN)
user_login.close()
