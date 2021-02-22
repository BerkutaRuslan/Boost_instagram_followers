from selenium import webdriver
import time
import chromedriver_binary
from selenium import webdriver
from selenium.common.exceptions import WebDriverException, TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from account_info import account_info, target_accounts
from utils import accounts_in_random_list, get_hrefs


class InstagramBot:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.browser = webdriver.Chrome()

    def close_browser(self):
        self.browser.close()

    def login_to_acc(self):
        browser = self.browser
        browser.get("https://www.instagram.com/")

        WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.XPATH, "//input[@name='username']")))
        login_field = browser.find_element_by_xpath("//input[@name='username']")
        login_field.send_keys(self.username)

        password_field = browser.find_element_by_xpath("//input[@name='password']")
        password_field.send_keys(self.password)
        password_field.send_keys(Keys.RETURN)
        try:
            WebDriverWait(browser, 2).until(
                EC.element_to_be_clickable((By.XPATH, "//button[@class='aOOlW  bIiDR  ']")))
            notification_window_submit_button = browser.find_element_by_xpath(
                "//button[@class='aOOlW  bIiDR  ']").click()
        except TimeoutException:
            WebDriverWait(browser, 10).until(
                EC.element_to_be_clickable((By.XPATH, "//button[@class='sqdOP  L3NKy   y3zKF     ']")))
            notification_window_submit_button = \
                browser.find_element_by_xpath("//button[@class='sqdOP  L3NKy   y3zKF     ']").click()
            WebDriverWait(browser, 10).until(
                EC.element_to_be_clickable((By.XPATH, "//button[@class='aOOlW  bIiDR  ']")))
            notification_window_submit_button = \
                browser.find_element_by_xpath("//button[@class='aOOlW  bIiDR  ']").click()

    def stealing_clients_with_likes(self, target, acc_amount_to_get):
        browser = self.browser
        browser.get(target)
        for i in range(1, 1):
            browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(1)
        pic_hrefs = get_hrefs(browser)

        for post in pic_hrefs:
            browser.get(post)
            WebDriverWait(browser, 10).until(EC.new_window_is_opened)
            all_who_liked = browser.find_element_by_css_selector("div.Nm9Fw > .zV_Nj")
            all_who_liked.click()
            time.sleep(0.5)
            all_who_liked.click()
            WebDriverWait(browser, 10).until(EC.new_window_is_opened)
            account_urls = []

            try:
                for i in range(1, 20):
                    element_inside_pop = browser.find_element_by_xpath('//div[@class="_1XyCr"]//a')
                    element_inside_pop.send_keys(Keys.END)
                    time.sleep(0.5)
                    account_hrefs_from_likes_list = \
                        browser.find_elements_by_xpath('//*[@class="FPmhX notranslate MBL3Z"]')
                    account_hrefs_2 = [element.get_attribute('href') for element in account_hrefs_from_likes_list]
                    account_hrefs_2 = [account_urls.append(href) for href in account_hrefs_2 if href not
                                       in account_urls]
                    time.sleep(0.5)
                    with open("unique_profiles.txt", "a") as account_profiles:
                        if sum(1 for line in open('unique_profiles.txt')) < acc_amount_to_get:
                            append_to_file = [account_profiles.write(element + "\n") for element in account_urls]
                        else:
                            print(f'"Уже {acc_amount_to_get} ссылок на профили в файле, выключаю"')
                            browser.close()
                            quit()
                print(f' Всего людей было добавлено в тхт файл на момент принта {len(account_urls)} "\n"')
            except Exception as e:
                print('error', e)
                pass

    def send_likes(self, amount_of_likes):
        try:
            browser = self.browser
            account_sum = sum(1 for line in open('unique_profiles.txt'))
            all_accounts = accounts_in_random_list("unique_profiles.txt", account_sum)
            all_liked_accounts = open('all_liked_accounts.txt', 'r')
            all_liked_accounts_profiles = all_liked_accounts.readlines()
            likes_was_made = 0
            for account in all_accounts:
                if account not in all_liked_accounts_profiles:
                    if likes_was_made <= amount_of_likes:
                        browser.get(account)
                        pic_hrefs = get_hrefs(browser)
                        liked_photo = 0
                        for pic_href in pic_hrefs:
                            if liked_photo < 2:
                                try:
                                    browser.get(pic_href)
                                    like_button = browser.find_element_by_css_selector("[height='24'][aria-label='Нравится']")
                                    like_button.click()
                                    liked_photo += 1
                                    likes_was_made += 1
                                    time.sleep(18)
                                    print(f'{likes_was_made} Всего поставили лайков')
                                except Exception as e:
                                    pass
                            else:
                                liked_accs_2 = open('liked_accounts.txt', "a")
                                liked_accs_2.write(account + '\n')
                                liked_accs_2.close()
                                liked_photo = 0
                                break
                    else:
                        browser.close()
                        exit()
                else:
                    pass
        except WebDriverException:
            self.browser.close()


# Get People accounts
# instagram = InstagramBot(username=account_info['insta_username'], password=account_info['insta_password'])
# instagram.login_to_acc()
# for target in target_accounts:
#     instagram.stealing_clients_with_likes(target, 1000)


# Get People accounts
# instagram = InstagramBot(username=account_info['insta_username'], password=account_info['insta_password'])
# instagram.login_to_acc()
# for target in target_accounts:
#     instagram.stealing_clients_with_likes(target, 1000)


# Send likes
instagram = InstagramBot(username=account_info['insta_username'], password=account_info['insta_password'])
instagram.login_to_acc()
instagram.send_likes(300)

