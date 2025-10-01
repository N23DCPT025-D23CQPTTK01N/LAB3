from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Cấu hình driver và URL trang login
URL = "file:///Users/jun/Downloads/LAB/login.html"  # Đường dẫn tuyệt đối tới file login.html

def setup_driver():
    # Đường dẫn tới chromedriver, chỉnh lại nếu bạn để ở vị trí khác
    service = Service("/Applications/chromedriver-mac-arm64/chromedriver")
    driver = webdriver.Chrome(service=service)
    driver.get(URL)
    return driver

def test_login_success(driver):
    driver.find_element(By.ID, "username").send_keys("sv1@ptit.edu.vn")
    driver.find_element(By.ID, "password").send_keys("P@ssw0rd")
    driver.find_element(By.ID, "btnLogin").click()
    time.sleep(2)
    # Kiểm tra đã chuyển hướng sang dashboard.html
    assert "dashboard.html" in driver.current_url

def test_login_wrong_password(driver):
    driver.find_element(By.ID, "username").clear()
    driver.find_element(By.ID, "password").clear()
    driver.find_element(By.ID, "username").send_keys("sv1@ptit.edu.vn")
    driver.find_element(By.ID, "password").send_keys("sai_pass")
    driver.find_element(By.ID, "btnLogin").click()
    time.sleep(1)
    error_msg = driver.find_element(By.ID, "msg-error")
    assert error_msg.is_displayed() and "Invalid credentials" in error_msg.text

def test_login_empty_fields(driver):
    driver.find_element(By.ID, "username").clear()
    driver.find_element(By.ID, "password").clear()
    driver.find_element(By.ID, "btnLogin").click()
    time.sleep(1)
    error_msg = driver.find_element(By.ID, "msg-error")
    assert error_msg.is_displayed() and "Please fill all required fields." in error_msg.text

def test_forgot_password_link(driver):
    forgot_link = driver.find_element(By.ID, "linkForgot")
    assert forgot_link.is_displayed()
    forgot_link.click()
    time.sleep(1)
    # Kiểm tra điều hướng hoặc hiển thị trang quên mật khẩu
    assert "Quên mật khẩu" in driver.page_source or "forgot" in driver.current_url

def test_signup_link(driver):
    signup_link = driver.find_element(By.ID, "linkSignup")
    assert signup_link.is_displayed()
    signup_link.click()
    time.sleep(1)
    assert "Đăng ký" in driver.page_source or "signup" in driver.current_url

def test_social_login_buttons(driver):
    fb = driver.find_element(By.ID, "btnFacebook")
    tw = driver.find_element(By.ID, "btnTwitter")
    gg = driver.find_element(By.ID, "btnGoogle")
    assert fb.is_displayed() and tw.is_displayed() and gg.is_displayed()
    assert fb.is_enabled() and tw.is_enabled() and gg.is_enabled()

def run_all_tests():
    driver = setup_driver()
    try:
        test_login_success(driver)
        driver.get(URL)
        test_login_wrong_password(driver)
        driver.get(URL)
        test_login_empty_fields(driver)
        driver.get(URL)
        test_forgot_password_link(driver)
        driver.get(URL)
        test_signup_link(driver)
        driver.get(URL)
        test_social_login_buttons(driver)
        # Lưu ảnh màn hình kết quả cuối cùng
        driver.save_screenshot('ketqua.png')
        print("Tất cả test case đã chạy xong! Đã lưu ảnh màn hình vào ketqua.png")
    finally:
        driver.quit()

if __name__ == "__main__":
    run_all_tests()
