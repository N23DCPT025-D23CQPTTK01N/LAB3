<<<<<<< HEAD
# LAB3
=======
# Selenium Login Form Test

## Mô tả
- Tự động kiểm thử form đăng nhập với 6 test case bằng Selenium Python.
- Form mẫu: login.html

## Hướng dẫn chạy test
1. Cài đặt Python và Selenium:
   ```
   pip install selenium
   ```
2. Cài đặt ChromeDriver (hoặc Firefox geckodriver) phù hợp với trình duyệt.
3. Chạy server cục bộ (khuyến nghị):
   ```
   python -m http.server 8000
   ```
   Sau đó truy cập: http://localhost:8000/login.html
4. Chạy test:
   ```
   python test_login_form.py
   ```

## Test case
1. Đăng nhập thành công (username: sv1@ptit.edu.vn, password: P@ssw0rd)
2. Sai mật khẩu
3. Bỏ trống trường
4. Click link Forgot password?
5. Click link SIGN UP
6. Kiểm tra 3 nút social login (Facebook, Twitter, Google)

## Locator
- Sử dụng By.ID cho các trường input, button, link.
- Sử dụng By.CLASS_NAME hoặc By.TAG_NAME cho các thành phần khác nếu cần.

## Ảnh chụp kết quả
- Lưu ảnh màn hình khi chạy test bằng Selenium:
  ```python
  driver.save_screenshot('result.png')
  ```
- Ảnh sẽ lưu tại thư mục hiện tại.
>>>>>>> 855fd50 (Add selenium test, use case, screenshot, and docs)
