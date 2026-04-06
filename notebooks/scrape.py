from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import streamlit as st
import time
from os import environ
from selenium.webdriver import Remote, ChromeOptions as Options
from selenium.webdriver.chromium.remote_connection import ChromiumRemoteConnection as Connection
from bs4 import BeautifulSoup


def scrape_website(website):

    print("Launching the Chrome browser...")
  

    AUTH = st.secrets["AUTH"]

    if not AUTH:
        raise Exception("Missing AUTH credentials. Set AUTH environment variable.")
   
    print('Connecting to Browser...')
    server_addr = f'https://{AUTH}@brd.superproxy.io:9515'
    connection = Connection(server_addr, 'goog', 'chrome')
    options = Options()
    options.add_argument("--headless=new")
    driver = Remote(connection, options=options)
    try:
        print(f'Connected! Navigating to {website}...')
        driver.get(website)
        print('Navigated! Scraping page content...')
        data = driver.page_source
        print(f'Scraped! Data: {data[:500]}...')
        return data  
    
    except Exception as e:
        print(f"Scraping failed: {e}")
        return "" 
        


    # # path to chromedriver.exe
    # chrome_driver_path = "./drivers/chromedriver.exe"

    # # Chrome options
    # options = webdriver.ChromeOptions()
    # # options.add_argument("--headless")  # optional: run without opening the browser

    # # Service object
    # service_obj = Service(chrome_driver_path)

    # # start the driver
    # driver = webdriver.Chrome(service=service_obj, options=options)

    # try:
    #     driver.get(website)
    #     print("Page loaded...")
    #     html = driver.page_source
    #     time.sleep(5)
    #     return html
    finally:
        driver.quit()


# Extracting the body content using beautiful soup

def extract_body_content(html_content):
    soup=BeautifulSoup(html_content,"html.parser")
    body_content=soup.body

    if body_content:
        return str(body_content)
    return ""


# clean the body content

def clean_body_content (body_content):
    soup=BeautifulSoup(body_content,"html.parser")

    for script_or_style in soup(["script","style"]):
        script_or_style.extract()
    
    cleaned_content=soup.get_text(separator="\n")
    cleaned_content="\n".join(
        line.strip() for line in cleaned_content.splitlines() if line.strip()
    )

    return cleaned_content

# Splitting the content into chunks

def split_dom_content(dom_content, chunk_size=6000):
    return [
        dom_content[i:i+chunk_size] for i in range(0, len(dom_content), chunk_size)
    ]


