import time
import math
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver

links = ["https://stepik.org/lesson/236895/step/1",     
         "https://stepik.org/lesson/236896/step/1",
         "https://stepik.org/lesson/236897/step/1",
         "https://stepik.org/lesson/236898/step/1",
         "https://stepik.org/lesson/236899/step/1",
         "https://stepik.org/lesson/236903/step/1",
         "https://stepik.org/lesson/236904/step/1",
         "https://stepik.org/lesson/236905/step/1"]

#secret_text = ""

@pytest.mark.parametrize("link", links)
class TestParametrization():

    def setup_method(self):
        print("\nstart browser for test...")
        self.browser = webdriver.Chrome()

    def teardown_method(self):
        print("\nquit browser for test...")
        self.browser.quit()

    def test_(self, link):
        self.browser.get(link)
        area_for_input = WebDriverWait(self.browser, 5).until(
        EC.presence_of_element_located((By.TAG_NAME, "textarea")))
        answer = math.log(int(time.time()))
        area_for_input.send_keys(str(answer))
        
        button = self.browser.find_element_by_tag_name("button")
        button.click()

        additional_feedback = WebDriverWait(self.browser, 10).until(
        EC.presence_of_element_located((By.TAG_NAME, "pre")))
        text = additional_feedback.text

        assert text == "Correct!", "Additional feedback does not contain text 'Correct', instead it says {}".format(text)
