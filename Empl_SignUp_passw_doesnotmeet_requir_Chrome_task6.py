#signup if password does not meet requirements
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get("http://3.23.148.163/")

#find get started button and click on it
get_star_btn = WebDriverWait(driver, 25).until(EC.element_to_be_clickable((By.XPATH, "//a[@href='/session/signin']")))
get_star_btn.click()

#find I am an employee button and click on it
emp_btn = WebDriverWait(driver, 25).until(EC.element_to_be_clickable((By.XPATH, "//div[2]/div[1]/button[1]")))
emp_btn.click()

#click sign_up button
signup_btn = WebDriverWait(driver, 25).until((EC.element_to_be_clickable((By.XPATH, "//div[3]/button/span[1]"))))
signup_btn.click()

#enter email signinemail@mailru
email_input_fld = WebDriverWait(driver, 25).until((EC.visibility_of_element_located((By.NAME, "email"))))
email_input_fld.send_keys("signinemail@mailru")

#enter Company Name 2 Bee Co
comp_name = WebDriverWait(driver, 25).until((EC.visibility_of_element_located((By.NAME, "companyName"))))
comp_name.send_keys("Name 2 Bee Co")

#enter password which does not meet requirements 123abc
pass_input_fld = WebDriverWait(driver, 25).until((EC.visibility_of_element_located((By.NAME, "password"))))
pass_input_fld.send_keys("1test")

#enter Full Name Boris Allot
name_input_fld = WebDriverWait(driver, 25).until((EC.visibility_of_element_located((By.NAME, "yourName"))))
name_input_fld.send_keys("Boris Allot")

#password must be at least 6 characters message has to be displayed
pass_err = WebDriverWait(driver, 25).until((EC.element_to_be_clickable((By.XPATH, "//div[3]/div/p"))))

#Password meet requirements, but user able to continue signingUp

driver.quit()