import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time  # No es necesario pero lo puse para que se pueda apreciar mejor el flujo.

class TestKatalon(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(10)  # Espera implícita de 10 segundos

    def test_katalon(self):
        # Log in
        driver = self.driver
        driver.get("https://katalon-demo-cura.herokuapp.com/")
        driver.save_screenshot('screenshot.png')
        time.sleep(2) # Para apreciasion visual de la accion (se puede eliminar)

        # Make appoinment
        Home_xpath = driver.find_element(By.XPATH, '//*[@id="btn-make-appointment"]')
        Home_xpath.click()
        driver.save_screenshot('screenshot2.png')
        time.sleep(2) # Para apreciasion visual de la accion (se puede eliminar)

        # Username
        demo_name_xpath = driver.find_element(By.XPATH, '//*[@id="login"]/div/div/div[2]/form/div[1]/div[1]/div/div/input')
        demo_name = demo_name_xpath.get_attribute('value')
        name_input = driver.find_element(By.XPATH, '//*[@id="txt-username"]')
        name_input.send_keys(demo_name)
        driver.save_screenshot('screenshot3.png')
        time.sleep(2) # Para apreciasion visual de la accion (se puede eliminar)

        # Password
        demo_name_xpath = driver.find_element(By.XPATH, '//*[@id="login"]/div/div/div[2]/form/div[1]/div[2]/div/div/input')
        demo_name = demo_name_xpath.get_attribute('value')
        name_input = driver.find_element(By.XPATH, '//*[@id="txt-password"]')
        name_input.send_keys(demo_name)
        driver.save_screenshot('screenshot4.png')
        time.sleep(2) # Para apreciasion visual de la accion (se puede eliminar)

        # Loggin click
        loggin = driver.find_element(By.XPATH, '//*[@id="btn-login"]')
        loggin.click()
        driver.save_screenshot('screenshot5.png')
        time.sleep(2) # Para apreciasion visual de la accion (se puede eliminar)

        # Select facility
        des_elem = driver.find_element(By.XPATH, '//*[@id="combo_facility"]')
        des_elem.click()
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="combo_facility"]/option[3]'))).click()
        driver.save_screenshot('screenshot6.png')
        time.sleep(2) # Para apreciasion visual de la accion (se puede eliminar)

        # Apply for hospital readmision
        readmission = driver.find_element(By.XPATH, '//*[@id="appointment"]/div/div/form/div[2]/div/label')
        readmission.click()
        driver.save_screenshot('screenshot7.png')
        time.sleep(2) # Para apreciasion visual de la accion (se puede eliminar)

        # select Healtcare Program
        h_progm = driver.find_element(By.XPATH, '//*[@id="appointment"]/div/div/form/div[3]/div/label[2]')
        h_progm.click()
        driver.save_screenshot('screenshot8.png')
        time.sleep(2) # Para apreciasion visual de la accion (se puede eliminar)

        # Set date
        date = driver.find_element(By.XPATH, '//*[@id="txt_visit_date"]')
        date.click()
        driver.save_screenshot('screenshot9.png')
        time.sleep(2) # Para apreciasion visual de la accion (se puede eliminar)
        set_month = driver.find_element(By.XPATH, '/html/body/div/div[1]/table/thead/tr[2]/th[3]')
        set_month.click()
        time.sleep(2) # Para apreciasion visual de la accion (se puede eliminar)
        driver.save_screenshot('screenshot10.png')
        set_day = driver.find_element(By.XPATH, '/html/body/div/div[1]/table/tbody/tr[2]/td[7]')
        set_day.click()
        driver.save_screenshot('screenshot11.png')
        time.sleep(2) # Para apreciasion visual de la accion (se puede eliminar)

        # Add comments
        comment = driver.find_element(By.XPATH, '//*[@id="txt_comment"]')
        comment.click()
        comment.send_keys('Ing. Diego Fernando Castellanos Vargas')
        driver.save_screenshot('screenshot12.png')
        time.sleep(2) # Para apreciasion visual de la accion (se puede eliminar)

        # Click book appointment button
        book_appointment = driver.find_element(By.XPATH, '//*[@id="btn-book-appointment"]')
        book_appointment.click()
        driver.save_screenshot('screenshot13.png')
        time.sleep(2) # Para apreciasion visual de la accion (se puede eliminar)

        # Click go to Home 
        go_to_home = driver.find_element(By.XPATH, '//*[@id="summary"]/div/div/div[7]/p/a')
        go_to_home.click()
        driver.save_screenshot('screenshot14.png')
        time.sleep(2) # Para apreciasion visual de la accion (se puede eliminar)

    def tearDown(self):
        self.driver.close()

if __name__ == '__main__':
    unittest.main()
