from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By

def load_webpage():
    chrome_options = Options()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-dev-shm-usage')

    driver = webdriver.Chrome(options=chrome_options)  # Optional argument, if not specified will search path.
    driver.get('https://lostmerchants.com/')

    sleep(10)
    html = driver.execute_script("return document.getElementsByTagName('html')[0].innerHTML")

    server_region = Select(driver.find_element(by=By.XPATH, value='//*[@id="severRegion"]'))
    server_region.select_by_value('NAE')

    server = Select(driver.find_element(by=By.XPATH, value='//*[@id="server"]'))
    server.select_by_visible_text('Zosma')

    table = driver.find_element(by=By.XPATH, value='/html/body/div[1]/div/div[2]/table')

    marchent_info = []
    for row in table.find_elements(by=By.CSS_SELECTOR, value='tr'):
        marchent_info.append([col.text for col in row.find_elements(by=By.CSS_SELECTOR, value='td')])

    driver.quit() # quit and close

    return marchent_info[1:]

print(load_webpage())