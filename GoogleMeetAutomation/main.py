from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import keys as K
import time
from prompt import Prompt

promp = Prompt()

chrome_options = Options()
chrome_options.add_argument("--use-fake-ui-for-media-stream")
chrome_options.add_argument("--disable-notifications")
chrome_web_driver = "" # YOUR CHROME DRIVER PATH
driver = webdriver.Chrome(executable_path=chrome_web_driver, options=chrome_options)
meeting_link = promp.get_link()
login_link = "https://accounts.google.com/signin/v2/identifier?hl=en&passive=true&continue=https%3A%2F%2Fwww.google.com%2F&ec=GAZAmgQ&flowName=GlifWebSignIn&flowEntry=ServiceLogin"
driver.get(login_link)
email_textbox = driver.find_element_by_id("identifierId")
email_textbox.send_keys(K.EMAIL)
email_textbox.send_keys(Keys.ENTER)
time.sleep(2)
password_textbox = driver.find_element_by_name("password")
password_textbox.send_keys(K.PASSWORD)
password_textbox.send_keys(Keys.ENTER)
time.sleep(2)
driver.get(url=meeting_link)
get_body = driver.find_element_by_tag_name("body")
get_body.send_keys(Keys.CONTROL + "d")
get_body.send_keys(Keys.CONTROL + "e")
time.sleep(1)
get_button = driver.find_element_by_xpath('//*[@id="yDmH0d"]/c-wiz/div/div/div[9]/div[3]/div/div/div[2]/div/div[1]/div[2]/div/div[2]/div/div[1]/div[1]/span')
get_button.click() 