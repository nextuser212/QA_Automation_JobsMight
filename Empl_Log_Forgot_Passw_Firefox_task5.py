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

#click on Forgot Password
forgot_btn = WebDriverWait(driver, 25).until(EC.element_to_be_clickable((By.XPATH, "//div[4]/button/span[1]")))
forgot_btn.click()

#enter email
email_fld = WebDriverWait(driver, 25).until(EC.element_to_be_clickable((By.XPATH, "//input[@name='email']")))
email_fld.send_keys("info@company2betest4.com")

#click on reset password
reset_pass_btn = WebDriverWait(driver, 25).until(EC.element_to_be_clickable((By.XPATH, "//div[2]/button[1]")))
reset_pass_btn.click()

#instructions for password reset message will be displayed

driver.quit()