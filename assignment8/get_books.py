from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager   
from selenium.webdriver.chrome.service import Service

import pandas as pd
import json
import time

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

url = 'https://durhamcounty.bibliocommons.com/v2/search?query=learning%20spanish&searchType=smart'
driver.get(url)

time.sleep(5)

book_entries = driver.find_elements(
    By.CSS_SELECTOR,
    'li.cp-search-result-item'
)

print(len(book_entries))

results = []

for book in book_entries:
    title = book.find_element(
        By.CLASS_NAME,
        'title-content'
    ).text

    authors = book.find_elements(
        By.CLASS_NAME,
        'author-link'
    )

    author_names = []

    for a in authors:
        author_names.append(a.text)

    authors_text = '; '.join(author_names)

    format_year = book.find_element(
        By.CLASS_NAME,
        'display-info-primary'
    ).text

    book_dictionary = {
        'title': title,
        'author': authors_text,
        'format_year': format_year
    }

    results.append(book_dictionary)

df = pd.DataFrame(results)

print (df)

df.to_csv('get_books.csv', index=False)

with open('get_books.json', 'w') as f:
    json.dump(results, f, indent=4)

    driver.quit()