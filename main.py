import pretty_errors
import time
import pickle
from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
from config import auth_data, ip


def get_data():
    url = "https://www.avito.ru/arhangelsk/kvartiry/sdam/na_dlitelnyy_srok-ASgBAgICAkSSA8gQ8AeQUg?context" \
          "=H4sIAAAAAAAA_0q0MrSqLraysFJKK8rPDUhMT1WyLrYyNLNSKk5NLErOcMsvyg3PTElPLVGyrgUEAAD__xf8iH4tAAAA&f" \
          "=ASgBAQICAkSSA8gQ8AeQUgFAzAg0kFmOWYxZ "
    options = webdriver.ChromeOptions()

    # proxy
    options.add_argument(f'--proxy-server={ip}')

    # disable webdriver mode
    options.add_argument("--disable-blink-features=AutomationControlled")

    # headless mode
    # options.add_argument("--headless")

    # browser opening
    browser = webdriver.Chrome(
        executable_path=r'D:\Work\Selenium Occurrence\chromedriver.exe',
        options=options
    )

    try:
        browser.get(url=url)

        ads = browser.find_elements(by=By.XPATH, value="//div[@class='iva-item-content-rejJg']")

        data = []
        for ad in ads:
            ad.click()
            browser.switch_to.window(browser.window_handles[1])
            ad_content = {'url': browser.current_url}
            price = browser.find_elements(by=By.XPATH, value='//span[@itemprop="price"]')
            ad_content['price'] = price[1].text
            user = browser.find_element(by=By.XPATH, value='//div[@data-marker="seller-info/label"]')
            ad_content['user'] = user.text
            data.append(ad_content)
            browser.close()
            browser.switch_to.window(browser.window_handles[0])

        for el in data:
            print(el)

    except Exception as ex:
        print(ex)
    finally:
        browser.close()
        browser.quit()


def main():
    get_data()


if __name__ == '__main__':
    main()
