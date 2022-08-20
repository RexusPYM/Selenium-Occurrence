import pretty_errors
import time
import datetime
from selenium import webdriver
from selenium.webdriver.common.by import By
from multiprocessing import Pool

urls_list = ["https://www.avito.ru/arhangelsk/kvartiry/sdam/na_dlitelnyy_srok-ASgBAgICAkSSA8gQ8AeQUg?context" 
             "=H4sIAAAAAAAA_0q0MrSqLraysFJKK8rPDUhMT1WyLrYyNLNSKk5NLErOcMsvyg3PTElPLVGyrgUEAAD__xf8iH4tAAAA&f"
             "=ASgBAQICAkSSA8gQ8AeQUgFAzAg0kFmOWYxZ ",
             "https://www.avito.ru/arhangelsk/tovary_dlya_kompyutera/komplektuyuschie/videokarty-ASgBAgICAkTGB"
             "~pm7gmmZw?cd=1",
             "https://www.avito.ru/arhangelsk/tovary_dlya_kompyutera/komplektuyuschie/protsessory-ASgBAgICAkTGB"
             "~pm7gniZw?cd=1"]


def get_data(url):

    options = webdriver.ChromeOptions()

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
        start_time = datetime.datetime.now()

        browser.get(url=url)
        amount_ads = 5
        ads = browser.find_elements(by=By.XPATH, value='//div[@data-marker="item"]')

        data = []
        for ad in ads:
            if len(data) < amount_ads:
                ad.click()
                browser.switch_to.window(browser.window_handles[1])

                ad_content = {'url': browser.current_url,
                              'price': browser.find_elements(by=By.XPATH,
                                                             value='//span[@itemprop="price"]')[-1].text,
                              'user': browser.find_element(by=By.XPATH,
                                                           value='//div[@data-marker="seller-info/label"]').text}
                data.append(ad_content)
                browser.close()
                browser.switch_to.window(browser.window_handles[0])
            else:
                break

        finish_time = datetime.datetime.now()
        spent_time = finish_time - start_time
        print(spent_time)

        for el in data:
            print(el)

    except Exception as ex:
        print(ex)
    finally:
        browser.close()
        browser.quit()


def main():
    pass


if __name__ == '__main__':
    p = Pool(processes=len(urls_list))
    p.map(get_data, urls_list)
