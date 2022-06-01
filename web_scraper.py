from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

# Set up web scraper
def init_scraper(query):
    service = Service("../../chromedriver/stable/chromedriver")
    driver = webdriver.Chrome(service=service)
    return driver

def process_search():
    title = 'SmartApply Job Search'
    print('-' * len(title) + '\n' + title + '\n' + '-' * len(title))
    query = input("What jobs do you want to look for today? > ")
    encoded = query.replace(' ', '%20')
    return encoded

def scrape_indeed(driver, query):
    driver.get(f"https://www.indeed.com/jobs?q={query}")
    print("Scraping Indeed...\n")
    postings = driver.find_elements(By.CLASS_NAME, "cardOutline")
    
    for posting in postings:
        title = posting.find_element(By.CLASS_NAME, "jcs-JobTitle").find_element(By.TAG_NAME, "span").text
        company = posting.find_element(By.CLASS_NAME, "companyOverviewLink").text
        print(title)
        print(company)
        print()


if __name__ == "__main__":
    query = process_search()
    driver = init_scraper(query)
    scrape_indeed(driver, query)
    
    driver.close()