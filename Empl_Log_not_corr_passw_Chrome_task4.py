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

#enter email
email_input_field = WebDriverWait(driver, 25).until((EC.visibility_of_element_located((By.NAME, "email"))))
email_input_field.send_keys("info@company2betest4.com")

#enter password
pass_input_field = WebDriverWait(driver, 25).until((EC.visibility_of_element_located((By.NAME, "password"))))
pass_input_field.send_keys("P123")

#click LogIn button
login_btn = WebDriverWait(driver, 25).until(EC.element_to_be_clickable((By.XPATH, "//div[3]/div")))
login_btn.click()

#error signin message should be displayed
err_btn = WebDriverWait(driver, 25).until(EC.element_to_be_clickable((By.XPATH, "//h6")))

driver.quit()