from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

import pandas as pd
import time
import re

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

url = "https://owasp.org/Top10/2025/"
driver.get(url)

time.sleep(5)

items = driver.find_elements(
    By.XPATH,
    "//a[contains(@href, '/A') and contains(@href, '_2025-') and starts-with(text(), 'A')]"
)


results = []

for item in items:
    title = item.text
    link = item.get_attribute("href")
   
    if re.match(r"A\d{2}:2025", title):
        results.append({
            "title": title,
            "link": link
        })

df = pd.DataFrame(results)

print(df)

df.to_csv("owasp_top_10.csv", index=False)

driver.quit()