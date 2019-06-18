import math
from selenium import webdriver


def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))


link = "https://suninjuly.github.io/execute_script.html"
browser = webdriver.Chrome()
browser.get(link)

x_element = browser.find_element_by_id("input_value")
x = x_element.text
y = calc(x)

browser.execute_script("window.scrollBy(0, 100);")

input_area = browser.find_element_by_id("answer")
input_area.send_keys(y)

check_box = browser.find_element_by_id("robotCheckbox")
check_box.click()

radio_button = browser.find_element_by_id("robotsRule")
radio_button.click()

button = browser.find_element_by_tag_name("button")
button.click()