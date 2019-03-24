from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.support.ui import WebDriverWait

driver = webdriver.Chrome(executable_path="E:/Software/chromedriver.exe")
driver.get("https://www.hotstar.com/sports/cricket/vivo-ipl-2019/kolkata-knight-riders-vs-sunrisers-hyderabad-m189953/live-streaming/2001710506?lang=eng")

driver.delete_all_cookies()


