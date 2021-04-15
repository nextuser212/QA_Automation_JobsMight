from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Firefox()

driver.get("http://3.23.148.163/")

#find get startet button and click on it
get_star_btn = WebDriverWait(driver, 25).until(EC.element_to_be_clickable((By.XPATH, "//a[@href='/session/signin']")))
get_star_btn.click()
#find I am an employee button and click on it
empl_btn = WebDriverWait(driver, 25).until(EC.element_to_be_clickable((By.XPATH, "//div[2]/div[1]/button[1]")))
empl_btn.click()
#enter email
email_input_field = WebDriverWait(driver, 25).until((EC.visibility_of_element_located((By.NAME, "email"))))
email_input_field.send_keys("nastv@mail.ru")

#enter password
pass_input_field = WebDriverWait(driver, 25).until((EC.visibility_of_element_located((By.NAME, "password"))))
pass_input_field.send_keys("123Abc&@")

#find Login button and click on it
login_btn = WebDriverWait(driver, 25).until(EC.element_to_be_clickable((By.XPATH, "//div[3]/div")))
login_btn.click()

driver.quit()