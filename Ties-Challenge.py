from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

LOW_BAL_STUD_ID = 62

driver = webdriver.Firefox()  # Geckodriver
driver.get("http://ties-software.github.io/QA/CodeChallenge/AddBalance.html")

wait = WebDriverWait(driver, 10)
wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'input.addAmount')))

# Grab all non-header rows of the student table
rows = driver.find_elements_by_css_selector("#add-amount-table > tbody > tr")

if len(rows) is 0:
    print("No students available to add balance.")
    quit()
# iterate through, to find the student we want, keep a reference of their entire row
for row in rows:
    student_id = row.find_element_by_css_selector("td[data-bind~=studentId]").text
    student_id = int(student_id)
    if student_id is LOW_BAL_STUD_ID:
        low_bal_row = row
        break

# grab current (starting) balance
starting balance = float(low_bal_row.find_element_by_css_selector("td[title=balance]").text)

# add some money to Low Balance
AMOUNT = 93
add_bal_input = low_bal_row.find_element_by_css_selector("td input.addAmount")
add_bal_input.send_keys(AMOUNT)

# Precautionary, make sure the 'Confirm' button has loaded
wait = WebDriverWait(driver, 10)
wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#update")))

confirm_btn = driver.find_element_by_css_selector("#update")
confirm_btn.click()

# grab new displayed balance
new_bal = float(acct_bal_ele.text)

assert new_bal == starting_bal + AMOUNT, "Wrong amount added. Current balance should be " + str(starting_bal + AMOUNT)

driver.quit()
