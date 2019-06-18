from selenium import webdriver
from selenium.webdriver.support.ui import Select

browser = webdriver.Chrome()
link = "http://suninjuly.github.io/selects1.html"
browser.get(link)

number1 = browser.find_element_by_id("num1")
number2 = browser.find_element_by_id("num2")

sum_ = int(number1.text) + int(number2.text)

select = Select(browser.find_element_by_tag_name("select"))
select.select_by_value(str(sum_))

button = browser.find_element_by_tag_name("button")
button.click()
