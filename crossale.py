import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import NoSuchElementException
import pickle
import time
from urllib.parse import urlparse, parse_qs

class CrossSaleAutomation:
    def __init__(self, user_obccos):
        self.chrome_driver_path = r"D:\ThangTGM\Tool\PYTHON\chromedriver-win64\chromedriver.exe"
        self.user_profile_path = r"D:\ThangTGM\Tool\PYTHON\chromedriver-win64\chromedriver.exe" + user_profile_name
        self.driver = None

    def init_driver(self):
        chrome_options = Options()
        chrome_options.add_argument(f"user-data-dir={self.user_profile_path}")
        chrome_options.add_argument("--headless")
        chrome_options.add_argument("--disable-gpu")
        chrome_options.add_argument("--window-size=1920x1080")
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--disable-dev-shm-usage")

        try:
            service = Service(self.chrome_driver_path)
            self.driver = webdriver.Chrome(service=service, options=chrome_options)
        except Exception as e:
            print(f"Lỗi khi khởi tạo WebDriver: {e}")
            exit(1)

    def login_to_system(self, username, password):
        try:
            self.driver.get("http://ccos.vnpt.vn/Login.aspx")
            time.sleep(4)

            if self.driver.title != "Đăng nhập hệ thống SSO VNPT":
                print("Session đã đăng nhập, không cần đăng nhập lại.")
                return {
                    "LoginSuccess": True,
                    "NeedOTP": False,
                    "Messenger": "Session đã đăng nhập, không cần đăng nhập lại."
                }

            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.ID, "txtUsername"))
            )

            username_field = self.driver.find_element(By.ID, "txtUsername")
            password_field = self.driver.find_element(By.ID, "txtPassword")

            username_field.send_keys(username)
            password_field.send_keys(password)

            login_button = self.driver.find_element(By.ID, "btnLogin")
            login_button.click()
            time.sleep(3)

            WebDriverWait(self.driver, 10).until(
                EC.url_changes("http://loginccos.vnpt.vn/Login.aspx")
            )
            print("Đăng nhập thành công!")

            current_url = self.driver.current_url
            
            return {
                "LoginSuccess": True,
                "NeedOTP": True,
                "Messenger": "Đăng nhập thành công, yêu cầu nhập OTP.",
                "ConfirmOTPUrl": current_url
            }

        except TimeoutException:
            print("Trang tải quá lâu hoặc không tìm thấy phần tử!")
            return {
                "LoginSuccess": False,
                "NeedOTP": False,
                "Messenger": "Trang tải quá lâu hoặc không tìm thấy phần tử!",
                "ConfirmOTPUrl": ""
            }
        except Exception as e:
            print(f"Lỗi khi đăng nhập: {e}")
            return {
                "LoginSuccess": False,
                "NeedOTP": False,
                "Messenger": f"Lỗi khi đăng nhập: {str(e)}",
                "ConfirmOTPUrl": ""
            }

    def enter_otp(self, url, otp):
        try:
            self.driver.get("http://ccos.vnpt.vn/Login.aspx")
            time.sleep(4)

            otp_field = self.driver.find_element(By.ID, "txtOtp")
            otp_field.send_keys(otp)

            process_button = self.driver.find_element(By.ID, "btnProcess")
            process_button.click()

            WebDriverWait(self.driver, 10).until(
                EC.invisibility_of_element((By.XPATH, "//*[contains(text(), 'Kiểm tra, xác nhận OTP')]"))
            )
            print("Xác nhận OTP thành công!")
            return {
                "VerifySuccess": True,
                "Messenger": f"Xác nhận OTP thành công!"
            }

        except TimeoutException:
            print("Xác nhận OTP không thành công, vẫn thấy dòng 'Kiểm tra, xác nhận OTP'.")
            return {
                "VerifySuccess": False,
                "Messenger": f"Xác nhận OTP không thành công, vẫn thấy dòng 'Kiểm tra, xác nhận OTP'."
            }

        except Exception as e:
            print(f"Lỗi khi nhập OTP: {e}")
            return {
                "VerifySuccess": False,
                "Messenger": f"Lỗi khi nhập OTP: {e}"
            }

    def navigate_to_customer_info(self, url):
        try:
            self.driver.get(url)
            print("Đã điều hướng đến trang Thông tin Khách hàng.")
        except Exception as e:
            print(f"Lỗi khi điều hướng: {e}")

    def logout(self):
        try:
            try:
                logout_button = WebDriverWait(self.driver, 10).until(
                    EC.element_to_be_clickable((By.LINK_TEXT, "Đăng xuất"))
                )
                logout_button.click()
                print("Đang thực hiện đăng xuất...")
            except Exception:
                logout_button = WebDriverWait(self.driver, 10).until(
                    EC.element_to_be_clickable((By.LINK_TEXT, "Thoát"))
                )
                logout_button.click()
                print("Đang thực hiện thoát...")

            time.sleep(10)

            WebDriverWait(self.driver, 10).until(EC.title_is("Đăng nhập hệ thống SSO VNPT"))
            print("Đăng xuất thành công!")
            return True

        except Exception as e:
            print(f"Lỗi khi đăng xuất: {e}")
            return False

    def gia_han(self, url):
        try:
            parsed_url = urlparse(url)
            query_params = parse_qs(parsed_url.query)

            ten_kh = query_params.get('TEN_KH', [''])[0]
            source = query_params.get('Source', [''])[0]

            self.driver.get(url)
            time.sleep(3)

            if self.driver.title != "CrossSell - Đăng ký dịch vụ":
                print("Không phải trang gia hạn dịch vụ!")
                return {
                    "GiaHanThanhCong": False,
                    "Messenger": f"Không phải trang gia hạn dịch vụ! URL bạn cung cấp chưa chính xác"
                }

            WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, "#popup_name > table > tbody > tr:nth-child(14) > td:nth-child(2) > div > a:nth-child(2)"))
            ).click()
            print("Click vào tùy chọn đầu tiên thành công.")

            WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, "#popup_name > table > tbody > tr:nth-child(15) > td:nth-child(2) > div > a:nth-child(2)"))
            ).click()
            print("Click vào tùy chọn thứ hai thành công.")

            WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.ID, "btnKhoaMoDV"))
            ).click()
            print("Click vào nút 'Khoa/Mở Dịch Vụ' thành công.")
            time.sleep(4)

            WebDriverWait(self.driver, 10).until(
                EC.frame_to_be_available_and_switch_to_it((By.CSS_SELECTOR, "iframe"))
            )
            print("Chuyển vào iframe thành công.")

            gia_han_buttons = self.driver.find_elements(By.XPATH, "//a[text()='Gia hạn gói đang sử dụng']")
            
            num_buttons = len(gia_han_buttons)
            print(f"Đã tìm thấy {num_buttons} nút 'Gia hạn gói đang sử dụng'.")
            
            if(num_buttons == 0):
                return {
                    "GiaHanThanhCong": False,
                    "Messenger": f"Không tìm thấy nút gia hạn."
                }

            for button in gia_han_buttons:
                data_type = button.get_attribute("data-type")
                data_csid = button.get_attribute("data-csid")
                data_sothuebao = button.get_attribute("data-sothuebao")
                data_loaithuebao = button.get_attribute("data-loaithuebao")
                data_package = button.get_attribute("data-package")

                data = {
                    "type": "GhPackage",
                    "tb": data_sothuebao,
                    "csid": data_csid,
                    "loaithuebao": data_loaithuebao,
                    "package": data_package
                }

                print(f"Gửi yêu cầu gia hạn với dữ liệu: {data}")
                # Giả lập quá trình gửi request

            return True

        except Exception as e:
            print(f"Lỗi khi gia hạn: {e}")
            return False
