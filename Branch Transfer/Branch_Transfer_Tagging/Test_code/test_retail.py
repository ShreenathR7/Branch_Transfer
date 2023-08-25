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
  
    
   
    def test_BranchTransfer_tagging(self,booting_function):   
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
        self.driver.find_element(by=By.XPATH,value=locators.Logi_Locators().Lot_No).click()
        sleep(5)
        lot_no = self.driver.find_element(by=By.XPATH,value=locators.Logi_Locators().text_box)
        lot_no.send_keys('7959')
        lot_no.send_keys(Keys.RETURN)
        sleep(5)
        self.driver.find_element(by=By.XPATH,value=locators.Logi_Locators().Section).click()
        sleep(5)
        section = self.driver.find_element(by=By.XPATH,value=locators.Logi_Locators().text_box)
        section.send_keys('GOLD EARRINGS')
        section.send_keys(Keys.RETURN)
        sleep(3)
        product = self.driver.find_element(By.ID, 'product')
        sleep(10)
        product.send_keys('RING &')
        sleep(5)
        product.send_keys(Keys.BACK_SPACE)
        sleep(10)
        se_ver = self.driver.find_elements(By.XPATH, "//ul[@id='ui-id-2']//li")
        print('Total',len(se_ver))
        for element in se_ver:
            if element.text == 'GB - RING & COIN':
                element.click()
                break
        sleep(5)
        self.driver.find_element(by=By.ID,value=locators.Logi_Locators().Tag_code).send_keys(data.Logi_Data().Tag_id)    
        sleep(8)
        self.driver.find_element(by=By.XPATH,value=locators.Logi_Locators().Search_button).click() 
        sleep(5)
        self.driver.find_element(by=By.ID,value=locators.Logi_Locators().add_preview).click()      
        sleep(5)
        self.driver.find_element(by=By.XPATH,value=locators.Logi_Locators().submit_tag_page).click()      
        assert self.driver.title == 'Logimax Technology | Admin'    
        print("Tagging item Branch Transfer Successfully From_Branch : {a},To_Branch : {b},Lot_No : {c},Section  : {d},Tag_code : {e} ". format(a ='Head OFFICE', b = 'CHINNA ANNAN JEWELLERY',c = '7959',  d ='GOLD EARRINGS',e = data.Logi_Data().Tag_id ))
      
   
   
    def test_BranchTransfer_tagging_another_way(self,booting_function):   
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
        self.driver.find_element(by=By.ID,value=locators.Logi_Locators().esti_no).send_keys(data.Logi_Data().esti_No)    
        sleep(5)
        self.driver.find_element(by=By.ID,value=locators.Logi_Locators().search_est).click()
        sleep(5)
        self.driver.find_element(by=By.NAME,value=locators.Logi_Locators().check_box).click()      
        sleep(5)
        self.driver.find_element(by=By.XPATH,value=locators.Logi_Locators().submit_tag_page).click()      
        assert self.driver.title == 'Logimax Technology | Admin'    
        print("Estimate No Using Tagging item Branch Transfer Successfully From_Branch : {a},To_Branch : {b},esti_no : {c}". format(a ='Head OFFICE', b = 'CHINNA ANNAN JEWELLERY',c  = data.Logi_Data().esti_No ))
        