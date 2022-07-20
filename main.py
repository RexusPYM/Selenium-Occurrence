import pretty_errors
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from config import auth_data, ip


def get_data():
    url = 'https://vk.com/'
    options = webdriver.ChromeOptions()

    # proxy
    options.add_argument(f'--proxy-server={ip}')

    # browser opening
    browser = webdriver.Chrome(
        executable_path=r'D:\Work\Selenium Occurrence\chromedriver.exe',
        options=options
    )

    def fill_auth_data(stage: str):
        data_input = browser.find_element(by=By.CSS_SELECTOR, value=f'[name={stage}]')
        data_input.clear()
        data_input.send_keys(auth_data[stage])
        time.sleep(0.5)
        data_input_button = browser.find_element(by=By.CSS_SELECTOR, value='[class="vkc__Button__container vkc__Button__primary vkc__Button__fluid"]')
        data_input_button.click()
        time.sleep(0.5)

    try:
        browser.get(url=url)
        time.sleep(0.5)

        login_button = browser.find_element(by=By.CSS_SELECTOR,
                                            value='[class="FlatButton FlatButton--primary FlatButton--size-l FlatButton--wide VkIdForm__button VkIdForm__signInButton"]')
        login_button.click()
        time.sleep(0.5)

        fill_auth_data('login')
        fill_auth_data('password')

        # login_input = browser.find_element(by=By.CSS_SELECTOR, value='[name="login"]')
        # login_input.clear()
        # login_input.send_keys(auth_data['login'])
        # time.sleep(0.5)
        # login_input_button = browser.find_element(by=By.CSS_SELECTOR, value='[class="vkc__Button__container vkc__Button__primary vkc__Button__fluid"]')
        # login_input_button.click()
        # time.sleep(0.5)
        #
        # password_input = browser.find_element(by=By.CSS_SELECTOR, value='[name="password"]')
        # password_input.clear()
        # password_input.send_keys(auth_data['password'])
        # time.sleep(0.5)
        # password_input_button = browser.find_element(by=By.CSS_SELECTOR, value='[class="vkc__Button__container vkc__Button__primary vkc__Button__fluid"]')
        # password_input_button.click()
        # time.sleep(0.5)

    except Exception as ex:
        print(ex)
    finally:
        browser.close()
        browser.quit()


def main():
    get_data()


if __name__ == '__main__':
    main()
