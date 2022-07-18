from selenium import webdriver
import time
from fake_useragent import UserAgent


def get_data():

    ip = ''  # text your proxy ip
    # url = 'https://www.whatismybrowser.com/detect/what-is-my-user-agent/'
    url = 'https://www.2ip.ru'
    options = webdriver.ChromeOptions()

    # change user-agent
    useragent = UserAgent()
    options.add_argument(f'user-agent={useragent.random}')

    # proxy
    options.add_argument(f'--proxy-server={ip}')

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
