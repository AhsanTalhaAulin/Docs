# Python program to demonstrate
# selenium
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities


driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))


driver.get("http://localhost:8069/web#cids=1&menu_id=5&action=37&model=ir.module.module&view_type=kanban")
driver.set_window_size(1440, 560)
driver.find_element(By.ID, "login").click()
driver.find_element(By.ID, "login").send_keys("hoque.talha@gmail.com")
driver.find_element(By.ID, "password").click()
driver.find_element(By.ID, "password").send_keys("Hww@1234")
driver.find_element(By.ID, "password").send_keys(Keys.ENTER)
driver.find_element(By.LINK_TEXT, "Update Apps List").click()
driver.find_element(By.CSS_SELECTOR, "div:nth-child(1) > .btn-primary > span").click()
driver.find_element(By.CSS_SELECTOR, ".oe_module_vignette:nth-child(28) .fa").click()
driver.find_element(By.CSS_SELECTOR, ".show > .dropdown-item:nth-child(2)").click()
element = driver.find_element(By.CSS_SELECTOR, ".oe_module_vignette:nth-child(28) > .oe_module_desc .btn")
actions = ActionChains(driver)
actions.move_to_element(element).perform()
