import unittest
import time
from selenium import webdriver


def check_registration(link):
    browser = webdriver.Chrome()
    browser.get(link)

    input1 = browser.find_element_by_css_selector(".first_block .first")
    input1.send_keys("Ivan")
    input2 = browser.find_element_by_css_selector(".first_block .second")
    input2.send_keys("Petrov")
    input3 = browser.find_element_by_css_selector(".first_block .third")
    input3.send_keys("mail@mail.ru")

    button = browser.find_element_by_css_selector("button.btn")
    button.click()

    time.sleep(1)

    welcome_text_elt = browser.find_element_by_tag_name("h1")
    welcome_text = welcome_text_elt.text
    
    return welcome_text


class TestRegistration(unittest.TestCase): 
    def test_registration1(self):
        link = "http://suninjuly.github.io/registration1.html"
        self.assertEqual(check_registration(link), "Поздравляем! Вы успешно зарегистировались!", "Registration failed")

    def test_registration2(self):
        link = "http://suninjuly.github.io/registration2.html"
        self.assertEqual(check_registration(link), "Поздравляем! Вы успешно зарегистировались!", "Registration failed")

if __name__ == "__main__":
    unittest.main()
