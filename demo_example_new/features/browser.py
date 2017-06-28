from selenium import webdriver
chrome_path ="/usr/local/lib/python3.5/site-packages/selenium/chromedriver"

class Browser(object):

    driver = webdriver.Chrome(chrome_path)
    driver.implicitly_wait(30)
    driver.set_page_load_timeout(30)
    driver.maximize_window()

    def close(context):
        context.driver.close()
