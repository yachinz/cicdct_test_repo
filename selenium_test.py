#! /usr/bin/python3
from argparse import ArgumentParser
from pyvirtualdisplay import Display
from random import random, randint
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
from threading import Thread, Lock
from yaml import safe_load


with open('resources/config.yaml') as yaml_in:
    config = safe_load(yaml_in)


class BrowserTest:
    def __init__(self):
        # self.browser = webdriver.Chrome(executable_path='E:/cs6620/proj/raw/driver/chromedriver.exe')
        self.browser = webdriver.Firefox(executable_path='./geckodriver.exe')

    def open_home(self):
        self.browser.set_page_load_timeout(30)
        self.browser.get(config['selenium_test_url'])
        sleep(randint(5, 10) + random())
        assert 'URL Shortener' in self.browser.title

    # test if the warning shows when the input is empty. Need some fix.
    def check_empty_link(self):
        # not show
        # assert len(self.browser.find_element_by_tag_name('Form.Control.Feedback')) == 0
        sleep(randint(1, 3) + random())
        self.browser.find_element_by_class_name('btn.btn-primary').click()
        assert self.browser.find_element_by_class_name('invalid-feedback').text == 'Please enter a valid URL.'
    
    def check_regular_link(self):
        # testcase1
        # https://github.com/yachinz/format_test
        # http://localhost:5000/aloEv2
        sleep(randint(1, 3) + random())
        self.browser.find_element_by_id('cloud_url_input').send_keys("https://github.com/yachinz/format_test")
        sleep(randint(1, 3) + random())
        self.browser.find_element_by_class_name('btn.btn-primary').click()
        sleep(randint(3, 5) + random())
        # check if this return a URL as wishes
        assert self.browser.find_element_by_id('cloud_url_output').get_attribute("value") == \
        'http://localhost:5000/aloEv2'
        sleep(randint(1, 3) + random())
        self.browser.find_element_by_id('cloud_url_input').clear()
        sleep(randint(1, 3) + random())

        # testcase2
        # https://github.com/yachinz/live2d-widget
        # http://localhost:5000/4nSynq
        self.browser.find_element_by_id('cloud_url_input').send_keys("https://github.com/yachinz/live2d-widget")
        sleep(randint(1, 3) + random())
        self.browser.find_element_by_class_name('btn.btn-primary').click()
        sleep(randint(3, 5) + random())
        # check if this return a URL as wishes
        assert self.browser.find_element_by_id('cloud_url_output').get_attribute("value") == \
        'http://localhost:5000/4nSynq'
        sleep(randint(1, 3) + random())
        self.browser.find_element_by_id('cloud_url_input').clear()
        sleep(randint(1, 3) + random())

        # testcase3
        # https://github.com/yachinz/easy-animator
        # http://localhost:5000/1JbS5c
        self.browser.find_element_by_id('cloud_url_input').send_keys("https://github.com/yachinz/easy-animator")
        sleep(randint(1, 3) + random())
        self.browser.find_element_by_class_name('btn.btn-primary').click()
        sleep(randint(3, 5) + random())
        # check if this return a URL as wishes
        assert self.browser.find_element_by_id('cloud_url_output').get_attribute("value") == \
        'http://localhost:5000/1JbS5c'
        sleep(randint(1, 3) + random())
        self.browser.find_element_by_id('cloud_url_input').clear()
        sleep(randint(1, 3) + random())

        # testcase4 
        # github.com/yachinz/live2d-widget
        # http://localhost:5000/6UErY0
        self.browser.find_element_by_id('cloud_url_input').send_keys("github.com/yachinz/live2d-widget")
        sleep(randint(1, 3) + random())
        self.browser.find_element_by_class_name('btn.btn-primary').click()
        sleep(randint(3, 5) + random())
        # check if this return a URL as wishes
        assert self.browser.find_element_by_id('cloud_url_output').get_attribute("value") == \
        'http://localhost:5000/6UErY0'
        sleep(randint(1, 3) + random())
        self.browser.find_element_by_id('cloud_url_input').clear()
        sleep(randint(1, 3) + random())

    def check_redirect(self):
        # testcase1
        # https://github.com/yachinz/format_test
        # http://localhost:5000/aloEv2
        self.browser.get('http://localhost:5000/aloEv2')
        sleep(randint(5, 10) + random())
        assert self.browser.current_url == 'https://github.com/yachinz/format_test'


        # testcase2
        # https://github.com/yachinz/live2d-widget
        # http://localhost:5000/4nSynq
        self.browser.get('http://localhost:5000/4nSynq')
        sleep(randint(5, 10) + random())
        assert self.browser.current_url == 'https://github.com/yachinz/live2d-widget'


        # testcase3
        # https://github.com/yachinz/easy-animator
        # http://localhost:5000/1JbS5c
        self.browser.get('http://localhost:5000/1JbS5c')
        sleep(randint(5, 10) + random())
        assert self.browser.current_url == 'https://github.com/yachinz/easy-animator'


        # testcase4 
        # github.com/yachinz/live2d-widget
        # http://localhost:5000/6UErY0
        self.browser.get('http://localhost:5000/6UErY0')
        sleep(randint(5, 10) + random())
        assert self.browser.current_url == 'https://github.com/yachinz/live2d-widget'

    def close_browser(self):
        self.browser.quit()


# class ArgParser:
#     def __init__(self):
#         description = 'Usage: python3 selenium_test.py  '
#         parser = ArgumentParser(description=description)
#         parser.add_argument('-x', '--headless', required=False, action='store_true',
#                             help='add -x option to run in terminal only (no GUI)')
#         self.args = parser.parse_args()

#     def get_args(self):
#         return self.args


# class MultiBrowserTest(ArgParser):
#     def __init__(self, n):
#         super().__init__()

#         self.browsers = [None for _ in range(n)]
#         self.lock = Lock()

#     def _browser_thread(self, index):
#         new_browser = BrowserTest()
#         with self.lock:
#             self.browsers[index] = new_browser
#         new_browser.open_home()
#         # new_browser.check_heading()
#         new_browser.click_api()

#     def open_browsers(self):
#         try:
#             threads = []
#             for index in range(len(self.browsers)):
#                 current_thread = Thread(target=self._browser_thread, args=[index])
#                 current_thread.start()
#                 threads.append(current_thread)
#             _ = [fin_thread.join() for fin_thread in threads]
#         finally:
#             sleep(randint(60, 70) + random())
#             _ = [obj.close_browser() for obj in self.browsers if obj is not None]


if __name__ == '__main__':
    new_browser = BrowserTest()
    new_browser.open_home()
    # new_browser.check_empty_link()
    new_browser.check_regular_link()
    new_browser.check_redirect()
    new_browser.close_browser()

    # sel_test = MultiBrowserTest(1)
    # sel_test.open_browsers()
    # if not sel_test.get_args().headless:
    # if False:
    #     sel_test.open_browsers()
    # else:
    #     with Display():
    #         sel_test.open_browsers()
