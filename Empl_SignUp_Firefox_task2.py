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

#click sign_up button
signup_btn = WebDriverWait(driver, 25).until((EC.element_to_be_clickable((By.XPATH, "//div[3]/button/span[1]"))))
signup_btn.click()

#enter email signuptest@gmail.com
email_input_fld = WebDriverWait(driver, 25).until((EC.visibility_of_element_located((By.NAME, "email"))))
email_input_fld.send_keys("signup4test@gmail.com")

#enter company name Company 2 Test
comp_name = WebDriverWait(driver, 25).until((EC.visibility_of_element_located((By.NAME, "companyName"))))
comp_name.send_keys("Company 2 Test")

#enter password Test12345%
pass_input_fld = WebDriverWait(driver, 25).until((EC.visibility_of_element_located((By.NAME, "password"))))
pass_input_fld.send_keys("Test123456%")

#enter full name Ana Ana
name_input_fld = WebDriverWait(driver, 25).until((EC.visibility_of_element_located((By.NAME, "yourName"))))
name_input_fld.send_keys("Ana Anaa")

#click next
next_btn = WebDriverWait(driver, 25).until((EC.visibility_of_element_located((By.XPATH, "//div[2]/button[2]/span[1]"))))
next_btn.click()

#enter company website comapny2test.com
website_fld = WebDriverWait(driver, 25).until((EC.visibility_of_element_located((By.NAME, "companyWebsite"))))
website_fld.send_keys("company422test..com")

#enter zip code 60700
zip_fld = WebDriverWait(driver, 25).until((EC.visibility_of_element_located((By.NAME, "zipcode"))))
zip_fld.send_keys("60700")

#enter phone numner
p_fld = WebDriverWait(driver, 25).until((EC.visibility_of_element_located((By.XPATH, "//input[@class = 'PhoneInputInput']"))))
p_fld.send_keys(2242242424)

#click on your title section
ttl_fld = WebDriverWait(driver, 40).until((EC.visibility_of_element_located(By.XPATH, "//div[1]/form/div[4]/div/div/input")))
ttl_fld.click()

#select HR from drop-down menu
hr_btn = WebDriverWait(driver, 25).until((EC.visibility_of_element_located(By.XPATH, "//li[2]")))
hr_btn.click()

#click_next
next_btn = WebDriverWait(driver, 25).until((EC.visibility_of_element_located((By.XPATH, "//div[2]/button[2]/span[1]"))))
next_btn.click()

driver.quit()