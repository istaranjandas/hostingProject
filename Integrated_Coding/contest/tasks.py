
# from celery import shared_task
# from selenium import webdriver
# from docker import from_env

# @shared_task
# def scrape(url):
#     docker_client = from_env()
#     docker_client.containers.run("selenium/standalone-chrome", detach=True)
#     driver = webdriver.Remote(
#         command_executor='http://localhost:4444/wd/hub',
#         desired_capabilities={'browserName': 'chrome', 'javascriptEnabled': True})
#     driver.get(url)
#     # add your web scraping code here
#     driver.quit()
#     docker_client.containers.prune()
 
from celery import shared_task
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service

@shared_task
def scrape_website():
    service = Service('E:\project\Online Chat App\chromedriver')
    driver = webdriver.Chrome(service=service)

    # Open the CodeChef contests page
    driver.get("https://www.codechef.com/contests")
    print(driver.title)

    
    # wait for the table to load
    table = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.CLASS_NAME, '_dataTable__container_1c9os_369')))

    # get the rows from the table
    rows = table.find_elements(By.TAG_NAME, 'tr')

    # loop through the rows and print the data
    for row in rows[1:]:
        columns = row.find_elements(By.TAG_NAME, 'td')
        if len(columns) > 0:
            print(columns[0].text, columns[1].text, columns[2].text, columns[3].text, columns[4].text)

    # close the driver
    driver.quit()

    return "done"
    
