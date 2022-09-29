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

class TestAdsf():
  def setup_method(self, method):
    self.driver = webdriver.Chrome()
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_adsf(self):
    self.driver.get("http://localhost:8069/web#cids=1&menu_id=5&action=37&model=ir.module.module&view_type=kanban")
    self.driver.set_window_size(1440, 560)
    self.driver.find_element(By.CSS_SELECTOR, ".oe_topbar_name").click()
    self.driver.find_element(By.LINK_TEXT, "Log out").click()
    self.driver.find_element(By.ID, "login").click()
    self.driver.find_element(By.ID, "login").send_keys("hoque.talha@gmail.com")
    self.driver.find_element(By.ID, "password").click()
    self.driver.find_element(By.ID, "password").click()
    self.driver.find_element(By.ID, "password").send_keys("Hww@1234")
    self.driver.find_element(By.ID, "password").send_keys(Keys.ENTER)
    self.driver.close()
    self.driver.find_element(By.ID, "login").click()
    self.driver.find_element(By.ID, "login").send_keys("hoque.talha@gmail.com")
    self.driver.find_element(By.ID, "password").click()
    self.driver.find_element(By.ID, "password").send_keys("hww@1234")
    self.driver.find_element(By.ID, "password").send_keys(Keys.ENTER)
    self.driver.find_element(By.ID, "password").click()
    self.driver.find_element(By.ID, "password").send_keys("Hww@1234")
    self.driver.find_element(By.ID, "password").send_keys(Keys.ENTER)
    self.driver.close()
    self.driver.find_element(By.ID, "login").click()
    self.driver.find_element(By.ID, "login").send_keys("hoque.talha@gmail.com")
    self.driver.find_element(By.ID, "password").click()
    self.driver.find_element(By.ID, "password").send_keys("Hww@1234")
    self.driver.find_element(By.ID, "password").send_keys(Keys.ENTER)
    self.driver.close()
  