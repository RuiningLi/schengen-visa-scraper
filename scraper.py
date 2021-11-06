from contextlib import closing
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
import csv
from bs4 import BeautifulSoup
import dropbox
from datetime import date
import pandas as pd
import json


def login_tls(email: str, pwd: str, url: str, location: str, country: str):
    with closing(webdriver.Chrome(service=Service(ChromeDriverManager().install()))) as driver:
        driver.get(url)
        wait = WebDriverWait(driver, 100)
        driver.find_element(By.ID, "email").send_keys(email)
        driver.find_element(By.ID, "pwd").send_keys(pwd)
        driver.find_element(By.ID, "btn").click()
        wait.until(lambda driver: driver.find_element(By.CLASS_NAME, "take_appointment"))
        page = driver.page_source
        get_available_slots(page, location, country)


def get_available_slots(page, location: str, country: str):
    soup = BeautifulSoup(page, "html.parser")
    available_slots = soup.find_all("a", class_="dispo")
    slots = []
    for slot in available_slots:
        slot_date = slot.find_previous_siblings("span", class_="appt-table-d")[0].text
        slot_time = slot_date[:-3] + " " + slot_date[-3:] + " " + slot.text
        slots.append(slot_time)
    with open("available_slots.csv", "a", newline="") as csvfile:
        writer = csv.writer(csvfile, delimiter=" ", quotechar="|", quoting=csv.QUOTE_MINIMAL)
        writer.writerow([country + "/" + location] + slots)


def scrape_earliest_appointment_date_for_france(location: str) -> None:
    email, pwd, url = None, None, None
    with open('dummy_accounts.json') as f:
        accounts = json.load(f)
        email = accounts["france"][location]["accounts"][0]["email"]
        pwd = accounts["france"][location]["accounts"][0]["pwd"]
        url = accounts["france"][location]["url"]
    try:
        login_tls(email, pwd, url, location, "france")
    except:
        pass

def main():
    TOKEN = "piE-9Mx-6HQAAAAAAAAAAWU6Frt_9EttoZ4rpaDHcUEVDIXng940PDF4vA7hqMf_"
    dbx = dropbox.Dropbox(TOKEN)
    cache_up_to_date = False
    try:
        cache = dbx.files_download_to_file("available_slots.csv", "/available_slots.csv")
        cache_up_to_date = cache.client_modified.date() == date.today()
    except:
        pass
    if not cache_up_to_date:
        scrape_earliest_appointment_date_for_france("london")
        scrape_earliest_appointment_date_for_france("manchester")
        scrape_earliest_appointment_date_for_france("edinburgh")
        with open("available_slots.csv", "rb") as csvfile:
            dbx.files_upload(csvfile.read(), "/available_slots.csv")

if __name__ == "__main__":
    main()
