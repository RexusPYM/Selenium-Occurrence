import pretty_errors
import time
import pickle
from selenium import webdriver
from selenium.webdriver.common.by import By
from config import auth_data, ip


def get_data():
    url = 'https://intoli.com/blog/not-possible-to-block-chrome-headless/chrome-headless-test.html'
    options = webdriver.ChromeOptions()

    # proxy
    options.add_argument(f'--proxy-server={ip}')

    # disable webdriver mode
    options.add_argument("--disable-blink-features=AutomationControlled")

    # browser opening
    browser = webdriver.Chrome(
        executable_path=r'D:\Work\Selenium Occurrence\chromedriver.exe',
        options=options
    )

    try:
        browser.get(url=url)
        time.sleep(5)
    except Exception as ex:
        print(ex)
    finally:
        browser.close()
        browser.quit()


def main():
    get_data()


if __name__ == '__main__':
    main()
