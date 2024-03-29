# Generated by Selenium IDE





import pytest
import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from grpc import ServicerContext
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

class TestTest1():
  def setup_method(self, method):
    self.driver = webdriver.Chrome(service=ServicerContext(ChromeDriverManager().install()))
    self.vars = {}
  
  
  def test_test1(self):
    self.driver.get("http://localhost:8069/web#cids=1&menu_id=5&action=37&model=ir.module.module&view_type=kanban")
    self.driver.set_window_size(1440, 560)
    self.driver.find_element(By.ID, "login").click()
    self.driver.find_element(By.ID, "login").send_keys("hoque.talha@gmail.com")
    self.driver.find_element(By.ID, "password").click()
    self.driver.find_element(By.ID, "password").send_keys("Hww@1234")
    self.driver.find_element(By.ID, "password").send_keys(Keys.ENTER)
    self.driver.find_element(By.LINK_TEXT, "Update Apps List").click()
    self.driver.find_element(By.CSS_SELECTOR, "div:nth-child(1) > .btn-primary > span").click()
    self.driver.find_element(By.CSS_SELECTOR, ".oe_module_vignette:nth-child(28) .fa").click()
    self.driver.find_element(By.CSS_SELECTOR, ".show > .dropdown-item:nth-child(2)").click()
    element = self.driver.find_element(By.CSS_SELECTOR, ".oe_module_vignette:nth-child(28) > .oe_module_desc .btn")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).perform()
    self.driver.close()
  
