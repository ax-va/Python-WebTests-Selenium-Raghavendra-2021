import os
import pathlib
import sys
import time

from selenium.webdriver.common.by import By

# Get the package directory
package_dir = str(pathlib.Path(__file__).resolve().parents[1])
# Add the package directory into sys.path if necessary
if package_dir not in sys.path:
    sys.path.insert(0, package_dir)

# my modules
import utils.webdrivers as webdrivers
from utils.highlighter import Highlighter


driver = webdrivers.get_chromedriver()
highlighter = Highlighter(driver)
website_abspath = os.path.abspath("../webpages/employee-form/index.html")
driver.get("file:///" + website_abspath)
time.sleep(5)

# Find element with id
form_employee = driver.find_element(By.CSS_SELECTOR, "#EmployeeForm")
highlighter.highlight_and_wait(form_employee)

# Find child element
input_first = driver.find_element(By.CSS_SELECTOR, "#EmployeeForm input")
highlighter.highlight_and_wait(input_first)

# Find element if:
# it is the 2nd "input" child of the parent
input_second = driver.find_element(By.CSS_SELECTOR, "#EmployeeForm input:nth-of-type(2)")  # the same element as below
highlighter.highlight_and_wait(input_second)

# Find element if:
# 1) it is an "input" element;
# 2) it is the 3rd child of the parent
input_second = driver.find_element(By.CSS_SELECTOR, "#EmployeeForm input:nth-child(3)")  # the same element as above
# Highlight with another color
highlighter.highlight_and_wait(input_second)

button_submit = driver.find_element(By.CSS_SELECTOR, "#EmployeeForm *:last-child")
highlighter.highlight_and_wait(button_submit)

website_abspath = os.path.abspath("../webpages/apress/index.html")
driver.get("file:///" + website_abspath)
time.sleep(5)

# To find element with class
element = driver.find_element(By.CSS_SELECTOR, ".press")
highlighter.highlight_and_wait(element)

# To find element with multiple class
element = driver.find_element(By.CSS_SELECTOR, ".my-class")
highlighter.highlight_and_wait(element)
element = driver.find_element(By.CSS_SELECTOR, ".text-justify")
highlighter.highlight_and_wait(element)
element = driver.find_element(By.CSS_SELECTOR, ".my-class.text-justify")
highlighter.highlight_and_wait(element)

# To find with prefix
element = driver.find_element(By.CSS_SELECTOR, "p[id^='123']")
highlighter.highlight_and_wait(element)
# To find with suffix
element = driver.find_element(By.CSS_SELECTOR, "p[id$='123']")
highlighter.highlight_and_wait(element)
# To find with substring
element = driver.find_element(By.CSS_SELECTOR, "p[id*='_apress_']")
highlighter.highlight_and_wait(element)

# To find with many attributes
element = driver.find_element(By.CSS_SELECTOR, "p[class='container'][id='apress'][style='align-self:center;']")
highlighter.highlight_and_wait(element)

driver.quit()