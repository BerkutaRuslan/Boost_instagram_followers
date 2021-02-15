import random


def accounts_in_random_list(file_name, account_sum):
    with open(file_name) as account_profiles:
        account_sum = account_sum
        elements_to_show = account_sum - 1
        random_lines = account_profiles.read().splitlines()
        order = random.sample(range(1, account_sum), elements_to_show)
        random_lines_order = [random_lines[line] for line in order]
        return random_lines_order


def get_hrefs(browser):
    hrefs = browser.find_elements_by_tag_name('a')
    pic_hrefs = [element.get_attribute('href') for element in hrefs]
    pic_hrefs = [href for href in pic_hrefs if '.com/p/' in href]
    return pic_hrefs
