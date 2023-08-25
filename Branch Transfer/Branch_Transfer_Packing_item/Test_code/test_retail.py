# app.py - The main executable file
from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from pynput.keyboard import Key,Controller
from time import sleep
from Test_locators import locators
from Test_data import data
import pytest


class Test_Logimax:
    @pytest.fixture
    

    def booting_function(self):
       self.driver = webdriver.Edge(service=Service(EdgeChromiumDriverManager().install()))
       self.driver.get(data.Logi_Data().url)
       self.driver.maximize_window()
       self.driver.implicitly_wait(5)
  
    
   
    def test_BranchTransfer_Purchase_item(self,booting_function):   
        self.driver.find_element(by=By.NAME,value=locators.Logi_Locators().username_inputBox).send_keys(data.Logi_Data().username)
        self.driver.find_element(by=By.NAME,value=locators.Logi_Locators().password_inputBox).send_keys(data.Logi_Data().password)
        sleep(8)
        self.driver.find_element(by=By.XPATH,value=locators.Logi_Locators().signButton).click()
        sleep(5)
        self.driver.find_element(by=By.XPATH,value=locators.Logi_Locators().side_bar).click()
        sleep(8)
        self.driver.find_element(by=By.PARTIAL_LINK_TEXT,value=locators.Logi_Locators().Inventory_module).click()
        sleep(5)
        self.driver.find_element(by=By.PARTIAL_LINK_TEXT,value=locators.Logi_Locators().Branch_Transfer).click()
        sleep(6)
        self.driver.find_element(by=By.ID,value=locators.Logi_Locators().add_estimation).click()
        sleep(6)
        self.driver.find_element(by=By.ID,value=locators.Logi_Locators().Packing_item).click()
        sleep(5)
        self.driver.find_element(by=By.XPATH,value=locators.Logi_Locators().From_Branch).click()
        sleep(5)
        branch = self.driver.find_element(by=By.XPATH,value=locators.Logi_Locators().text_box)
        branch.send_keys('Head OFFICE')
        branch.send_keys(Keys.RETURN) 
        sleep(5)
        self.driver.find_element(by=By.XPATH,value=locators.Logi_Locators().To_Branch).click()
        sleep(5)
        To_branch = self.driver.find_element(by=By.XPATH,value=locators.Logi_Locators().text_box)
        To_branch.send_keys('CHINNA ANNAN JEWELLERY')
        To_branch.send_keys(Keys.RETURN) 
        sleep(5)
        self.driver.find_element(by=By.XPATH,value=locators.Logi_Locators().selected_items).click()
        sleep(5)
        items = self.driver.find_element(by=By.XPATH,value=locators.Logi_Locators().text_box)
        items.send_keys('COIN BOX')
        items.send_keys(Keys.RETURN) 
        sleep(5)
        self.driver.find_element(by=By.ID,value=locators.Logi_Locators().No_of_pcs).send_keys(data.Logi_Data().count) 
        sleep(5)
        self.driver.find_element(by=By.ID,value=locators.Logi_Locators().Add_button).click()
        sleep(5)
        self.driver.find_element(by=By.XPATH,value=locators.Logi_Locators().submit_tag_page).click()      
        assert self.driver.title == 'Logimax Technology | Admin'    
        print("Packing item Branch Transfer Successfully    From_Branch : {a}, To_Branch  : {b}, selected_items : {c}, No_of_pcs : {e} ". format(a ='Head OFFICE',  b = 'CHINNA ANNAN JEWELLERY',c = 'COIN BOX', e = data.Logi_Data().count ))
          
   