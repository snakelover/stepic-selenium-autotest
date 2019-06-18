import math
from selenium import webdriver

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))



link = "http://suninjuly.github.io/math.html"
browser = webdriver.Chrome()
browser.get(link)

x_element = browser.find_element_by_id("input_value")
x = x_element.text
y = calc(x)

input_area = browser.find_element_by_id("answer")
input_area.send_keys(y)

check_box = browser.find_element_by_css_selector("[for='robotCheckbox']")
check_box.click()

radio_button = browser.find_element_by_id("robotsRule")
radio_button.click()

button = browser.find_element_by_tag_name("button")
button.click()
