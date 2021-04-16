from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Firefox()

driver.get("http://3.23.148.163/")

#find get started button and click on it
get_star_btn = WebDriverWait(driver, 25).until(EC.element_to_be_clickable((By.XPATH, "//a[@href='/session/signin']")))
get_star_btn.click()

#find I am an employee button and click on it
emp_btn = WebDriverWait(driver, 25).until(EC.element_to_be_clickable((By.XPATH, "//div[2]/div[1]/button[1]")))
emp_btn.click()

#enter email happyemailtotest@mail.ru
email_input_field = WebDriverWait(driver, 25).until((EC.visibility_of_element_located((By.NAME, "email"))))
email_input_field.send_keys("happyemailtotest@yahoo.com")

#enter password Password098$
pass_input_field = WebDriverWait(driver, 25).until((EC.visibility_of_element_located((By.NAME, "password"))))
pass_input_field.send_keys("Password098$")

#click LogIn
login_btn = WebDriverWait(driver, 25).until(EC.element_to_be_clickable((By.XPATH, "//div[3]/div")))
login_btn.click()

#Error on SignIn window should be displayed
error_sign = WebDriverWait(driver, 25).until(EC.element_to_be_clickable((By.XPATH, "//div[3]/div/div[1]")))

driver.quit()