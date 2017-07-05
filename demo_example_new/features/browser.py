from selenium import webdriver
chrome_path =""/home/aj/Documents/chromedriver""

class Browser(object):

    driver = webdriver.Chrome(chrome_path)
    driver.implicitly_wait(30)
    driver.set_page_load_timeout(30)
    driver.maximize_window()

    def close(context):
        context.driver.close()
