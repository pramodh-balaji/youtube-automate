from selenium import webdriver
from selenium.webdriver.common.keys import Keys


search = str(input("what you want to search for:  "))
PATH = f'C:/Program Files (x86)/chromedriver.exe'
driver = webdriver.Chrome(PATH)
driver.get("https://youtube.com")
driver.maximize_window()

ele= driver.find_element_by_name('search_query')
ele.click()
ele.send_keys(search)
ele.send_keys(Keys.RETURN)



