from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options


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






