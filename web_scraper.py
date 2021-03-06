from selenium import webdriver, common
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support import expected_conditions as EC
import sys

# Set up web scraper
def init_scraper():
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

    jobs = []
    
    for posting in postings:
        # skip any easy apply listings for now
        try:
            easy_apply = posting.find_element(By.CLASS_NAME, "indeedApply")

            if easy_apply:
                print("Skipping Easy Apply")
                continue
        except common.exceptions.NoSuchElementException as error:
            pass

        title = posting.find_element(By.CLASS_NAME, "jcs-JobTitle").find_element(By.TAG_NAME, "span").text
        
        company = ''
        try:
            company = posting.find_element(By.CLASS_NAME, "companyOverviewLink").text
        except common.exceptions.NoSuchElementException as error:
            pass

        try:
            if company == None or company == '':
                company = posting.find_element(by=By.CLASS_NAME, value="companyName").text
        except common.exceptions.NoSuchElementException as error:
            print("Skipping ---- 55")
            continue

        posting.click()

        try:
            frame = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.ID, 'vjs-container-iframe'))
            )

            driver.switch_to.frame(frame)

            links = [elem.get_attribute("href") or '' for elem in driver.find_elements_by_partial_link_text("Apply on company site")]

            if len(links) < 1:
                continue

            print(links[0])
            driver.switch_to.default_content()

            print(title)
            print(company)
            print()

            jobs.append({"title": title, "company": company, "link": links[0]})
        except:
            print("Skipping ---- 81")
            continue
    
    return jobs

def call_from_app(query):
    driver = init_scraper()
    jobs = scrape_indeed(driver, query)
    driver.close()
    return jobs

if __name__ == "__main__":
    driver = init_scraper()
    query = process_search()
    scrape_indeed(driver, query)
    driver.close()