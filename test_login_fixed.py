import pytest
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options as ChromeOptions
import time


# ============================================================
TEST_EMAIL = os.environ.get("TEST_EMAIL")
TEST_PASSWORD = os.environ.get("TEST_PASSWORD")

@pytest.fixture
def driver():
    options = ChromeOptions()
    driver = webdriver.Chrome(options=options)
    driver.maximize_window()
    driver.get("https://yedion.jce.ac.il/yedion/fireflyweb.aspx?prgname=login")
    yield driver
    driver.quit()


def test_login_valid1(driver):
    wait = WebDriverWait(driver, 50)
    try:
        wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "כניסה למערכת"))).click()

        username = wait.until(EC.presence_of_element_located((By.ID, "i0116")))
        username.clear()
        username.send_keys(TEST_EMAIL)
        time.sleep(3)

        wait.until(EC.element_to_be_clickable((By.ID, "idSIButton9"))).click()

        password = wait.until(EC.presence_of_element_located((By.ID, "i0118")))
        password.clear()
        password.send_keys(TEST_PASSWORD)
        time.sleep(3)
        wait.until(EC.element_to_be_clickable((By.ID, "idSIButton9"))).click()
        time.sleep(3)

        # Waiting for MFA phone approval
        target_element = wait.until(
            EC.element_to_be_clickable(
                (By.XPATH, '//*[@id="idDiv_SAOTCS_Proofs"]/div[2]/div/div/div[2]/div')
            )
        )
        target_element.click()

        confirm_button = wait.until(
            EC.element_to_be_clickable((By.ID, "idSIButton9"))
        )
        confirm_button.click()

    except Exception as e:
        print("Test 1 Failed:", e)
        raise


# --- Test Case 2: Invalid Username ---
def test_invalid_username(driver):
    wait = WebDriverWait(driver, 50)
    try:
        wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "כניסה למערכת"))).click()

        username = wait.until(EC.presence_of_element_located((By.ID, "i0116")))
        username.clear()
        username.send_keys("invalid_user@post.jce.ac.il")
        time.sleep(3)
        wait.until(EC.element_to_be_clickable((By.ID, "idSIButton9"))).click()

        error = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="usernameError"]')))
        assert error.is_displayed(), "Test 2 Failed: Error message not shown."
        print("Test 2 Passed: Invalid username error shown.")

    except Exception as e:
        print("Test 2 Failed:", e)


# --- Test Case 3: Invalid Password ---
def test_invalid_password(driver):
    wait = WebDriverWait(driver, 50)
    try:
        wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "כניסה למערכת"))).click()

        username = wait.until(EC.presence_of_element_located((By.ID, "i0116")))
        username.clear()
        username.send_keys(TEST_EMAIL)
        time.sleep(3)
        wait.until(EC.element_to_be_clickable((By.ID, "idSIButton9"))).click()

        password = wait.until(EC.presence_of_element_located((By.ID, "i0118")))
        password.clear()
        password.send_keys("WrongPassword123*")
        time.sleep(3)
        wait.until(EC.element_to_be_clickable((By.ID, "idSIButton9"))).click()

        error = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="passwordError"]')))
        assert error.is_displayed(), "Test 3 Failed: Error message not shown."
        print("Test 3 Passed: Invalid password error shown.")

    except Exception as e:
        print("Test 3 Failed:", e)


# --- Test Case 4: Forgot Password Link ---
def test_click_forgot_password(driver):
    wait = WebDriverWait(driver, 50)
    try:
        wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "כניסה למערכת"))).click()

        username = wait.until(EC.presence_of_element_located((By.ID, "i0116")))
        username.clear()
        username.send_keys(TEST_EMAIL)
        time.sleep(3)
        wait.until(EC.element_to_be_clickable((By.ID, "idSIButton9"))).click()

        password = wait.until(EC.presence_of_element_located((By.ID, "i0118")))
        password.clear()
        password.send_keys("wrong pass")
        time.sleep(3)
        wait.until(EC.element_to_be_clickable((By.ID, "idSIButton9"))).click()

        element = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="idA_PWD_ForgotPassword"]'))
        )
        element.click()
        print("Test 4 Passed: Clicked on forgot password successfully.")

    except Exception as e:
        print("Test 4 Failed:", e)


# --- Test Case 5: Empty Username ---
def test_invalid_login(driver):
    wait = WebDriverWait(driver, 50)
    try:
        login_link = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "כניסה למערכת")))
        login_link.click()

        submit_btn = wait.until(EC.element_to_be_clickable((By.ID, "idSIButton9")))
        submit_btn.click()

        error = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="usernameError"]')))
        assert error.is_displayed(), "Test 5 Failed: Validation not displayed."
        print("Test 5 Passed: Empty fields error shown.")

    except Exception as e:
        print("Test 5 Failed:", e)


# --- Test Case 6: Valid Login via Phone Call ---
def test_login_valid2(driver):
    wait = WebDriverWait(driver, 50)
    try:
        wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "כניסה למערכת"))).click()

        username = wait.until(EC.presence_of_element_located((By.ID, "i0116")))
        username.clear()
        username.send_keys(TEST_EMAIL)
        time.sleep(3)
        wait.until(EC.element_to_be_clickable((By.ID, "idSIButton9"))).click()

        password = wait.until(EC.presence_of_element_located((By.ID, "i0118")))
        password.clear()
        password.send_keys(TEST_PASSWORD)
        time.sleep(3)
        wait.until(EC.element_to_be_clickable((By.ID, "idSIButton9"))).click()

        target_element = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(
                (By.XPATH, '//*[@id="idDiv_SAOTCS_Proofs"]/div[1]/div/div/div[2]/div')
            )
        )
        target_element.click()
        time.sleep(30)  # Wait for MFA phone call approval
        driver.find_element(By.ID, "idSubmit_SAOTCC_Continue").click()

        button = WebDriverWait(driver, 7).until(
            EC.element_to_be_clickable((By.ID, "idSIButton9"))
        )
        button.click()
        print("Test 6 Passed: Logged in successfully via phone call.")

    except Exception as e:
        print("Test 6 Failed:", e)


# --- Test Case 7: Invalid Verification Code ---
def test_login_invalid2(driver):
    wait = WebDriverWait(driver, 5)
    try:
        wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "כניסה למערכת"))).click()

        username = wait.until(EC.presence_of_element_located((By.ID, "i0116")))
        username.clear()
        username.send_keys(TEST_EMAIL)
        time.sleep(3)
        wait.until(EC.element_to_be_clickable((By.ID, "idSIButton9"))).click()

        password = wait.until(EC.presence_of_element_located((By.ID, "i0118")))
        password.clear()
        password.send_keys(TEST_PASSWORD)
        time.sleep(3)
        wait.until(EC.element_to_be_clickable((By.ID, "idSIButton9"))).click()

        target_element = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(
                (By.XPATH, '//*[@id="idDiv_SAOTCS_Proofs"]/div[1]/div/div/div[2]/div')
            )
        )
        target_element.click()
        time.sleep(5)

        text_box = wait.until(EC.presence_of_element_located((By.ID, "idTxtBx_SAOTCC_OTC")))
        text_box.clear()
        text_box.send_keys("12345")
        driver.find_element(By.ID, "idSubmit_SAOTCC_Continue").click()

        error = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="idSpan_SAOTCC_Error_OTC"]')))
        assert error.is_displayed(), "Test 7 Failed: Error message not shown."
        print("Test 7 Passed: Invalid verification code error shown.")

    except Exception as e:
        print("Test 7 Failed:", e)


# --- Test Case 8: Empty Verification Code ---
def test_login_invalid3(driver):
    wait = WebDriverWait(driver, 5)
    try:
        driver.get("https://yedion.jce.ac.il/yedion/fireflyweb.aspx?prgname=login")
        wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "כניסה למערכת"))).click()

        username = wait.until(EC.presence_of_element_located((By.ID, "i0116")))
        username.clear()
        username.send_keys(TEST_EMAIL)
        time.sleep(3)
        wait.until(EC.element_to_be_clickable((By.ID, "idSIButton9"))).click()

        password = wait.until(EC.presence_of_element_located((By.ID, "i0118")))
        password.clear()
        password.send_keys(TEST_PASSWORD)
        time.sleep(3)
        wait.until(EC.element_to_be_clickable((By.ID, "idSIButton9"))).click()

        target_element = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(
                (By.XPATH, '//*[@id="idDiv_SAOTCS_Proofs"]/div[1]/div/div/div[2]/div')
            )
        )
        target_element.click()
        time.sleep(3)
        driver.find_element(By.ID, "idSubmit_SAOTCC_Continue").click()

        error = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="idSpan_SAOTCC_Error_OTC"]')))
        assert error.is_displayed(), "Test 8 Failed: Error message not shown."
        print("Test 8 Passed: Empty verification code error shown.")

    except Exception as e:
        print("Test 8 Failed:", e)


# --- Test Case 9: New Student Login Link ---
def test_new_student_login_valid1(driver):
    try:
        driver.find_element(By.LINK_TEXT, "שכחתי סיסמה | סטודנט חדש").click()
        print("Test 9 Passed: New student link clicked.")
    except Exception as e:
        print("Test 9 Failed:", e)


# --- Test Case 10: Help Page Link ---
def test_helping_page_valid1(driver):
    try:
        driver.find_element(By.LINK_TEXT, "כאן").click()
        print("Test 10 Passed: Help page link clicked.")
    except Exception as e:
        print("Test 10 Failed:", e)


# === LOGIN FIXTURE ===
@pytest.fixture
def logged_in_driver(driver):
    wait = WebDriverWait(driver, 50)
    try:
        wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "כניסה למערכת"))).click()

        username = wait.until(EC.presence_of_element_located((By.ID, "i0116")))
        username.clear()
        username.send_keys(TEST_EMAIL)
        time.sleep(3)

        wait.until(EC.element_to_be_clickable((By.ID, "idSIButton9"))).click()

        password = wait.until(EC.presence_of_element_located((By.ID, "i0118")))
        password.clear()
        password.send_keys(TEST_PASSWORD)
        time.sleep(3)

        wait.until(EC.element_to_be_clickable((By.ID, "idSIButton9"))).click()
        time.sleep(3)

        # Waiting for MFA phone approval
        target_element = wait.until(EC.element_to_be_clickable(
            (By.XPATH, '//*[@id="idDiv_SAOTCS_Proofs"]/div[2]/div/div/div[2]/div')))
        target_element.click()

        confirm_button = wait.until(EC.element_to_be_clickable((By.ID, "idSIButton9")))
        confirm_button.click()

        return driver
    except Exception as e:
        print("Login fixture failed:", e)
        raise


# === POST-LOGIN TESTS ===

def test_check_assignments(logged_in_driver):
    driver = logged_in_driver
    wait = WebDriverWait(driver, 20)
    try:
        courses = wait.until(EC.element_to_be_clickable(
            (By.XPATH, "//span[text()='אתרי קורסים']/ancestor::button")))
        courses.click()

        assignments = wait.until(EC.element_to_be_clickable(
            (By.XPATH, '//*[@id="TMenu9"]/div/div[5]/button')))
        assignments.click()

        semester_dropdown = wait.until(EC.element_to_be_clickable(
            (By.XPATH, '//*[@id="select2-R1C2-container"]')))
        semester_dropdown.click()
        wait.until(EC.element_to_be_clickable((By.XPATH, "//li[text()='1']"))).click()

        year_dropdown = wait.until(EC.element_to_be_clickable(
            (By.XPATH, '//*[@id="select2-R1C5-container"]')))
        year_dropdown.click()
        wait.until(EC.element_to_be_clickable(
            (By.XPATH, "//li[contains(text(),'2023')]"))).click()

        year_button = wait.until(EC.element_to_be_clickable(
            (By.XPATH, '//*[@id="main-content"]/article/form/div[2]/input[1]')))
        year_button.click()

        expand_section = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="H3_1"]')))
        expand_section.click()

    except Exception as e:
        print("Test check_assignments Failed:", e)
        raise


def test_open_Model_site(logged_in_driver):
    driver = logged_in_driver
    wait = WebDriverWait(driver, 20)
    try:
        courses = wait.until(EC.element_to_be_clickable(
            (By.XPATH, "//span[text()='אתרי קורסים']/ancestor::button")))
        courses.click()
        time.sleep(1)

        model_button = wait.until(EC.element_to_be_clickable(
            (By.XPATH, '//*[@id="TMenu9"]/div/div[1]/button')))
        model_button.click()
        time.sleep(2)

        assert "moodle" in driver.current_url.lower() or "מודל" in driver.page_source
        print("Test open_Model_site Passed.")

    except Exception as e:
        print("Test open_Model_site Failed:", e)
        raise


def test_open_course_sites(logged_in_driver):
    driver = logged_in_driver
    wait = WebDriverWait(driver, 20)
    try:
        courses = driver.find_element(By.XPATH, "//span[text()='אתרי קורסים']/ancestor::button")
        courses.click()
        time.sleep(1)

        course_sites = driver.find_element(By.XPATH, '//*[@id="TMenu9"]/div/div[2]/button')
        course_sites.click()
        time.sleep(1)

        semester_dropdown = driver.find_element(By.XPATH, '//*[@id="select2-R1C2-container"]')
        semester_dropdown.click()
        time.sleep(1)
        driver.find_element(By.XPATH, "//li[text()='1']").click()
        time.sleep(1)

        year_dropdown = driver.find_element(By.XPATH, '//*[@id="select2-R1C1-container"]')
        year_dropdown.click()
        time.sleep(1)
        driver.find_element(By.XPATH, "//li[contains(text(), '2023')]").click()
        time.sleep(1)

        refresh_button = driver.find_element(
            By.XPATH, '//*[@id="main-content"]/article/form/div[1]/div[4]/a')
        refresh_button.click()
        time.sleep(5)

        driver.find_element(By.XPATH, '//*[@id="ID_20241"]').click()
        time.sleep(2)
        print("Test open_course_sites Passed.")

    except Exception as e:
        print("Test open_course_sites Failed:", e)
        raise
